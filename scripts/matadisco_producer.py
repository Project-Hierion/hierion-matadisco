#!/usr/bin/env python3
"""
Matadisco Producer — Publish records to the Matadisco decentralized data discovery network.

Usage:
    python scripts/matadisco_producer.py --validate --file docs/records/record.json
    python scripts/matadisco_producer.py --dry-run --file docs/records/record.json
    python scripts/matadisco_producer.py --publish --file docs/records/record.json
    python scripts/matadisco_producer.py --publish --dir docs/records/
    python scripts/matadisco_producer.py --publish --dir docs/records/ --spread
"""

import os
import sys
import json
import time
import argparse
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
PDS_URL = os.getenv("MATADISCO_PDS_URL", "https://bsky.social")
HANDLE = os.getenv("MATADISCO_HANDLE")
APP_PASSWORD = os.getenv("MATADISCO_APP_PASSWORD")
DRY_RUN = os.getenv("MATADISCO_DRY_RUN", "false").lower() == "true"
MIN_DELAY = float(os.getenv("MATADISCO_MIN_DELAY", "1.0"))
MAX_DELAY = float(os.getenv("MATADISCO_MAX_DELAY", "5.0"))
LOG_LEVEL = os.getenv("MATADISCO_LOG_LEVEL", "INFO")

# Setup logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper()),
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Constants
COLLECTION = "cx.vmx.matadisco"
LEXICON_LLMDATAHUB = "org.project-hierion.llmdatahub"
LEXICON_CADMIES = "org.project-hierion.cadmies"
LEXICON_MATADISCO = "cx.vmx.matadisco"


class MatadiscoProducer:
    """Producer for publishing records to Matadisco."""

    def __init__(self, pds_url: str, handle: str, app_password: str, dry_run: bool = False):
        self.pds_url = pds_url.rstrip("/")
        self.handle = handle
        self.app_password = app_password
        self.dry_run = dry_run
        self.did = None
        self.access_token = None
        self.refresh_token = None

    def authenticate(self) -> bool:
        """Authenticate with the PDS and obtain access tokens."""
        if self.dry_run:
            logger.info("🔍 DRY RUN: Skipping authentication")
            return True

        logger.info(f"🔐 Authenticating with {self.pds_url} as {self.handle}")

        try:
            response = requests.post(
                f"{self.pds_url}/xrpc/com.atproto.server.createSession",
                json={"identifier": self.handle, "password": self.app_password},
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()

            data = response.json()
            self.did = data.get("did")
            self.access_token = data.get("accessJwt")
            self.refresh_token = data.get("refreshJwt")

            logger.info(f"✅ Authenticated successfully (DID: {self.did})")
            return True

        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Authentication failed: {e}")
            if hasattr(e, "response") and e.response:
                logger.error(f"Response: {e.response.text}")
            return False

    def validate_record(self, record: Dict[str, Any]) -> bool:
        """Validate a record against its Lexicon."""
        record_type = record.get("$type")

        if not record_type:
            logger.error("❌ Record missing '$type' field")
            return False

        # Basic validation based on Lexicon
        if record_type == LEXICON_MATADISCO:
            return self._validate_matadisco(record)
        elif record_type == LEXICON_LLMDATAHUB:
            return self._validate_llmdatahub(record)
        elif record_type == LEXICON_CADMIES:
            return self._validate_cadmies(record)
        else:
            logger.error(f"❌ Unknown Lexicon: {record_type}")
            return False

    def _validate_matadisco(self, record: Dict[str, Any]) -> bool:
        """Validate basic Matadisco record."""
        required = ["resource", "publishedAt"]
        for field in required:
            if field not in record:
                logger.error(f"❌ Missing required field: {field}")
                return False
        logger.info("✅ Record validates against cx.vmx.matadisco Lexicon")
        return True

    def _validate_llmdatahub(self, record: Dict[str, Any]) -> bool:
        """Validate LLMDataHub record."""
        required = ["resource", "publishedAt", "project-hierion"]
        for field in required:
            if field not in record:
                logger.error(f"❌ Missing required field: {field}")
                return False

        # Validate project-hierion key
        ph = record.get("project-hierion", {})
        required_ph = ["datasetName", "organization", "authors", "license", 
                       "description", "source", "originalRepo", "attribution", "sourceDate"]
        for field in required_ph:
            if field not in ph:
                logger.error(f"❌ Missing required field in project-hierion: {field}")
                return False

        # Ensure tags don't contain redundant license info
        tags = record.get("tags", [])
        for tag in tags:
            if tag.endswith("-license"):
                logger.warning(f"⚠️ Redundant license tag found: {tag} (license is in project-hierion.license)")

        logger.info("✅ Record validates against project-hierion.llmdatahub Lexicon")
        return True

    def _validate_cadmies(self, record: Dict[str, Any]) -> bool:
        """Validate CADMIES record."""
        required = ["resource", "publishedAt", "cadmies"]
        for field in required:
            if field not in record:
                logger.error(f"❌ Missing required field: {field}")
                return False

        # Validate cadmies key
        c = record.get("cadmies", {})
        required_c = ["conceptName", "conceptId", "definition", "domains", 
                      "source", "attribution", "sourceDate"]
        for field in required_c:
            if field not in c:
                logger.error(f"❌ Missing required field in cadmies: {field}")
                return False

        # Validate resource is ipfs:// CID
        resource = record.get("resource", "")
        if not resource.startswith("ipfs://"):
            logger.warning(f"⚠️ Resource does not use ipfs:// URI: {resource}")

        logger.info("✅ Record validates against project-hierion.cadmies Lexicon")
        return True

    def publish_record(self, record: Dict[str, Any]) -> bool:
        """Publish a single record to Matadisco."""
        if self.dry_run:
            logger.info("🔍 DRY RUN — Record preview:")
            print(json.dumps(record, indent=2))
            return True

        if not self.access_token:
            logger.error("❌ Not authenticated. Call authenticate() first.")
            return False

        # Validate before publishing
        if not self.validate_record(record):
            return False

        try:
            logger.info(f"📤 Publishing record...")

            response = requests.post(
                f"{self.pds_url}/xrpc/com.atproto.repo.createRecord",
                json={
                    "collection": COLLECTION,
                    "repo": self.did,
                    "record": record
                },
                headers={
                    "Authorization": f"Bearer {self.access_token}",
                    "Content-Type": "application/json"
                }
            )

            # Check rate limit headers
            remaining = response.headers.get("ratelimit-remaining")
            reset = response.headers.get("ratelimit-reset")
            if remaining:
                logger.info(f"📊 Rate limit remaining: {remaining} (reset: {reset})")

            if response.status_code == 429:
                # Rate limit hit
                reset_time = int(reset) if reset else time.time() + 60
                wait_seconds = max(reset_time - time.time(), 1)
                logger.warning(f"⏳ Rate limit hit. Waiting {wait_seconds:.1f}s...")
                time.sleep(wait_seconds)
                # Retry once
                return self.publish_record(record)

            if response.status_code != 200:
                logger.error(f"❌ Server response: {response.text}")
                response.raise_for_status()

            data = response.json()
            uri = data.get("uri")
            logger.info(f"✅ Record published successfully: {uri}")
            return True

        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Failed to publish: {e}")
            if hasattr(e, "response") and e.response:
                logger.error(f"Response: {e.response.text}")
            return False

    def calculate_delay(self, index: int, total: int) -> float:
        """Calculate delay based on position in batch."""
        if total <= 1:
            return 0.0

        # Linear spread from MIN_DELAY to MAX_DELAY
        progress = index / (total - 1)
        delay = MIN_DELAY + (MAX_DELAY - MIN_DELAY) * progress
        return delay


def load_record(filepath: str) -> Optional[Dict[str, Any]]:
    """Load a JSON record from a file."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"❌ Failed to load {filepath}: {e}")
        return None


def load_records_from_dir(directory: str) -> List[Dict[str, Any]]:
    """Load all JSON records from a directory."""
    records = []
    path = Path(directory)
    for json_file in sorted(path.glob("*.json")):
        record = load_record(str(json_file))
        if record:
            records.append((str(json_file), record))
    return records


def main():
    parser = argparse.ArgumentParser(description="Matadisco Producer")
    parser.add_argument("--validate", action="store_true", help="Validate a record")
    parser.add_argument("--dry-run", action="store_true", help="Preview publishing without sending")
    parser.add_argument("--publish", action="store_true", help="Publish records")
    parser.add_argument("--file", help="Path to a single JSON record file")
    parser.add_argument("--dir", help="Directory containing JSON records")
    parser.add_argument("--spread", action="store_true", help="Spread publishing over time to respect rate limits")

    args = parser.parse_args()

    if not args.validate and not args.publish and not args.dry_run:
        parser.print_help()
        sys.exit(1)

    # Load records
    records = []
    if args.file:
        record = load_record(args.file)
        if record:
            records.append((args.file, record))
    elif args.dir:
        records = load_records_from_dir(args.dir)
    else:
        logger.error("❌ Please specify --file or --dir")
        sys.exit(1)

    if not records:
        logger.error("❌ No records loaded")
        sys.exit(1)

    # Validate mode (doesn't need credentials)
    if args.validate:
        logger.info(f"🔍 Validating {len(records)} record(s)...")
        producer = MatadiscoProducer(PDS_URL, "", "", dry_run=True)
        for filepath, record in records:
            logger.info(f"📄 {filepath}")
            producer.validate_record(record)
        return

    # Dry run or publish mode
    # Check credentials
    if not HANDLE or not APP_PASSWORD:
        logger.error("❌ Missing credentials. Set MATADISCO_HANDLE and MATADISCO_APP_PASSWORD in .env")
        sys.exit(1)

    producer = MatadiscoProducer(PDS_URL, HANDLE, APP_PASSWORD, dry_run=args.dry_run)

    # Authenticate (skip for dry run)
    if not args.dry_run:
        if not producer.authenticate():
            sys.exit(1)

    logger.info(f"📤 Publishing {len(records)} record(s)...")

    successful = 0
    for i, (filepath, record) in enumerate(records):
        logger.info(f"📄 {filepath} ({i+1}/{len(records)})")

        if producer.publish_record(record):
            successful += 1

        # Delay between publishes
        if args.spread and i < len(records) - 1:
            delay = producer.calculate_delay(i, len(records))
            logger.info(f"⏳ Waiting {delay:.1f}s before next publish...")
            time.sleep(delay)

    logger.info(f"📊 Summary: {successful}/{len(records)} published successfully")

    if successful < len(records):
        sys.exit(1)


if __name__ == "__main__":
    main()
