# Manual Run — Matadisco Producer

## Purpose

This document provides instructions for manually running the Matadisco producer to publish records.

## Prerequisites

Before running the producer manually, ensure:

- [ ] Environment is set up (see [Setup](setup.md))
- [ ] Virtual environment is activated
- [ ] `.env` file is configured with valid credentials
- [ ] Record files are prepared and validated

## Commands

### Validate a Record

Validate a record against its Lexicon without publishing:

```bash
python scripts/matadisco_producer.py --validate --file docs/records/test-dolphin-dataset.json
```

Example output:

text
✅ Record validates against Lexicon project-hierion.llmdatahub
Dry Run (Preview Only)
Preview what would be published without actually sending to ATProto:

bash
python scripts/matadisco_producer.py --dry-run --file docs/records/test-dolphin-dataset.json
Example output:

text
🔍 DRY RUN — Record preview:

{
  "$type": "project-hierion.llmdatahub",
  "resource": "https://huggingface.co/datasets/QuixiAI/dolphin",
  "publishedAt": "2023-07-01",
  ...
}

✅ Dry run complete. No records were published.
Publish a Single Record
Publish a single record to Matadisco:

bash
python scripts/matadisco_producer.py --publish --file docs/records/test-dolphin-dataset.json
Example output:

text
📤 Publishing record...
✅ Record published successfully: at://did:plc:.../cx.vmx.matadisco/abc123
Publish Multiple Records
Publish all records in a directory:

bash
python scripts/matadisco_producer.py --publish --dir docs/records/
Example output:

text
📤 Publishing 3 records from docs/records/...
✅ Published: test-dolphin-dataset.json
✅ Published: test-concept-anatta.json
✅ Published: test-concept-interconnectedness.json
📊 Summary: 3 published, 0 failed
Publish with Rate Limit Spreading
Publish records with delays to respect rate limits:

bash
python scripts/matadisco_producer.py --publish --dir docs/records/ --spread
Example output:

text
📤 Publishing 3 records with spreading...
⏳ Waiting 1.5s before next publish...
✅ Published: test-dolphin-dataset.json
⏳ Waiting 2.3s before next publish...
✅ Published: test-concept-anatta.json
⏳ Waiting 1.8s before next publish...
✅ Published: test-concept-interconnectedness.json
📊 Summary: 3 published, 0 failed
Complete Workflow Example
bash
# 1. Activate environment
source venv/bin/activate

# 2. Validate record
python scripts/matadisco_producer.py --validate --file docs/records/test-dolphin-dataset.json

# 3. Dry run
python scripts/matadisco_producer.py --dry-run --file docs/records/test-dolphin-dataset.json

# 4. Publish for real
python scripts/matadisco_producer.py --publish --file docs/records/test-dolphin-dataset.json
Troubleshooting
Issue	Solution
Authentication failed	Check MATADISCO_APP_PASSWORD in .env
Rate limit exceeded	Use --spread flag or increase delays
Invalid Lexicon	Verify record matches Lexicon schema
Network error	Check internet connection and retry
Validation failed	Review error message and fix record
Environment Variables Reference
Variable	Description	Default
MATADISCO_PDS_URL	PDS endpoint URL	https://bsky.social
MATADISCO_HANDLE	ATProto handle	(required)
MATADISCO_APP_PASSWORD	App password	(required)
MATADISCO_MIN_DELAY	Minimum delay between publishes (seconds)	1.0
MATADISCO_MAX_DELAY	Maximum delay between publishes (seconds)	5.0
MATADISCO_DRY_RUN	Preview mode without publishing	false
MATADISCO_LOG_LEVEL	Logging verbosity	INFO
Version History
Date	Version	Changes
2026-08-05	1.0	Initial manual run documentation
