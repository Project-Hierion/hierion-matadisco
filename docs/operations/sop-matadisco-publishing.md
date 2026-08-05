# SOP — Matadisco Publishing Workflow

## Purpose

This document defines the standard operating procedure for publishing records from Project Hierion to the Matadisco decentralized data discovery network (AT Protocol).

## Scope

This SOP covers:
- License auditing of datasets
- Schema validation
- Record preparation
- Publishing via the producer script
- Post-publishing verification

## Prerequisites

Before publishing, ensure:

- [ ] Dataset or concept has been license-audited (see License Audit SOP)
- [ ] Record schema matches the Lexicon definition
- [ ] All required fields are populated
- [ ] `$type` field references the correct Lexicon
- [ ] Resource URIs use proper format (ipfs:// or https://)
- [ ] Attribution is complete and accurate
- [ ] Environment variables are set (.env file)

## Workflow Steps

### Step 1: License Audit

1. Verify the dataset has an explicit open license
2. Confirm license is one of: MIT, Apache 2.0, CC-BY, BSD, GPL
3. Document in `docs/audit/license-audit.md`
4. If no license or restrictive license → SKIP (do not publish)

### Step 2: Prepare Record

1. Create JSON file in `docs/records/` or `data/` directory
2. Include core schema fields:
   - `$type`
   - `resource`
   - `publishedAt`
   - `tags`
   - `preview` (optional)
3. Include custom top-level key matching your tag:
   - `project-hierion` for datasets
   - `cadmies` for concepts
4. Validate against Lexicon schema

### Step 3: Schema Validation

Use the producer script to validate records before publishing:

```bash
python scripts/matadisco_producer.py --validate --file docs/records/test-dataset.json

Step 4: Dry Run
Run a dry-run to preview what will be published:

bash
python scripts/matadisco_producer.py --dry-run --file docs/records/test-dataset.json
Step 5: Publish
Publish the record:

bash
python scripts/matadisco_producer.py --publish --file docs/records/test-dataset.json
Step 6: Verify
Check the Matadisco network for the record

Confirm record appears with correct data

Log the publication in the publishing log

Rate Limit Compliance
Monitor rate limit headers returned by ATProto

If approaching limits, pause and resume after cooldown

Use spreading logic for bulk publishing

Default delay between publishes: 1-5 seconds

Publishing Log
Maintain a log of all published records:

markdown
| Date | Record | Type | Status | Notes |
|------|--------|------|--------|-------|
| 2026-07-31 | dolphin | dataset | Published | MIT license verified |
Rollback Procedure
If a record needs to be removed:

Use ATProto delete operation

Document the removal

Update publishing log

Version History
Date	Version	Changes
2026-08-05	1.0	Initial SOP definition
