# Experiment: Matadisco Publish Test

**Date:** 2026-08-05
**Phase:** 73
**Status:** Complete

## Objective

Publish test records to the Matadisco decentralized data discovery network to validate:
- Producer script functionality
- Schema structure with correct `$type` fields
- Authentication with self-hosted PDS
- Rate limit handling

## Setup

- **Environment:** GitHub Codespaces
- **PDS:** Self-hosted at `https://pds.project-hierion.org`
- **Account:** `gardener.pds.project-hierion.org`
- **Producer Script:** `scripts/matadisco_producer.py`
- **Dependencies:** Python 3, requests, python-dotenv, pydantic

## Procedure

### 1. Authentication Test

Authenticated with PDS using `com.atproto.server.createSession` endpoint.

**Result:** ✅ Success — Received access and refresh tokens.

### 2. Record Validation

Validated record structure against Lexicon schemas.

**Result:** ✅ Success — Records validated against:
- `cx.vmx.matadisco` (top-level)
- `project-hierion.llmdatahub` (custom dataset key)
- `project-hierion.cadmies` (custom concept key)

### 3. Dry Run

Performed dry run to preview record data without publishing.

**Result:** ✅ Success — Record preview displayed correctly.

### 4. Publish Test

Published three test records:

| Record | AT-URI | Status |
|--------|--------|--------|
| Dolphin Dataset | `at://did:plc:7dstfcw5vsfpluag7xzd7s2h/cx.vmx.matadisco/3msedzcgae22i` | ✅ Published |
| Anatta Concept | `at://did:plc:7dstfcw5vsfpluag7xzd7s2h/cx.vmx.matadisco/3msee3nm6lk2i` | ✅ Published |
| Interconnectedness Concept | `at://did:plc:7dstfcw5vsfpluag7xzd7s2h/cx.vmx.matadisco/3msee3vo3jc2i` | ✅ Published |

### 5. Verification

Verified records via PDS query:

```bash
curl https://pds.project-hierion.org/xrpc/com.atproto.repo.getRecord?collection=cx.vmx.matadisco&repo=did:plc:7dstfcw5vsfpluag7xzd7s2h&rkey=3msedzcgae22i
```

Result: ✅ Success — Full record data returned.

Results
All three test records published successfully. Rate limit headers returned with remaining quota: 2993-2997 remaining.

Key Finding: The $type field must be cx.vmx.matadisco at the top level, with the custom Lexicon ID nested inside the custom key as its own $type field.

Analysis
What Worked
Authentication with self-hosted PDS

Record validation against Lexicons

Publishing via com.atproto.repo.createRecord

Rate limit header monitoring

What We Learned
Top-level $type must be cx.vmx.matadisco for all Matadisco records

Custom Lexicon ID goes inside the custom key as $type

Example structure:
```
{
  "$type": "cx.vmx.matadisco",
  "resource": "...",
  "publishedAt": "...",
  "project-hierion": {
    "$type": "project-hierion.llmdatahub",
    ...
  }
}
```

Challenges
Initial publish failed with "Invalid $type" error

Root cause: top-level $type was project-hierion.llmdatahub instead of cx.vmx.matadisco

Fix applied and tested successfully

Conclusion
Phase 73 test records are live on Matadisco. The producer pipeline works end-to-end. Ready to scale up to bulk publishing.

Next Steps
Scale to publish remaining CADMIES concepts (636 total)

Audit and publish LLMDataHub datasets

Automate publishing with GitHub Actions

References

- [Matadisco GitHub](https://github.com/vmx/matadisco)
- [AT Protocol API Documentation](https://docs.bsky.app)
- [Project Hierion Matadisco Repo](https://github.com/Project-Hierion/hierion-matadisco)
