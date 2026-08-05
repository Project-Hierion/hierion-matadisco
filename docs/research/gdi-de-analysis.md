# Analysis — gdi-de-csw-to-atproto Reference Implementation

## Purpose

This document analyzes the `gdi-de-csw-to-atproto` repository, a reference implementation for publishing records to Matadisco. Understanding this codebase informs our own producer script design and rate limit handling strategy.

## Overview

`gdi-de-csw-to-atproto` is a GitHub Actions-based pipeline that publishes geospatial metadata records to Matadisco. It handles spikes in new records by spreading them out over time to respect AT Protocol rate limits.

**Repository:** [vmx/gdi-de-csw-to-atproto](https://github.com/vmx/gdi-de-csw-to-atproto)

## Key Patterns

### 1. GitHub Actions Automation

The repository uses scheduled GitHub Actions workflows to:
- Check for new records from the source (CSW endpoint)
- Generate Matadisco records from the data
- Publish them to the AT Protocol network

**Relevance to us:** This is the pattern vmx recommended for scaling. We can adopt the same approach for bulk publishing our 636 concepts and datasets.

### 2. Rate Limit Spreading

When a large batch of new records is detected, the pipeline spreads publishing over time to avoid hitting AT Protocol rate limits [citation:vmx-email].

**How it works:**
- Records are queued
- Publishing is staggered with calculated delays
- Rate limit headers are monitored
- Backoff is applied if limits are approached

**Relevance to us:** Our producer script already includes `--spread` functionality with configurable delays. We can tune this for bulk publishing.

### 3. AT Protocol Authentication

The repository handles authentication with a PDS using:
- `com.atproto.server.createSession` — Get access token
- Access token used for subsequent `com.atproto.repo.createRecord` calls

**Relevance to us:** We've implemented the same pattern in our producer script.

### 4. Record Generation

Records are generated from CSW metadata, mapping fields to the `cx.vmx.matadisco` schema.

**Relevance to us:** Our records are generated from LLMDataHub dataset metadata and CADMIES concepts — different sources, same core schema.

## What We Can Adopt

| Pattern | Our Implementation |
|---------|-------------------|
| GitHub Actions automation | Future: `./github/workflows/publish.yml` |
| Rate limit spreading | Current: `--spread` flag in producer script |
| Authentication pattern | Current: `authenticate()` method |
| Record validation | Current: `validate_record()` method |

## Differences

| Aspect | gdi-de-csw-to-atproto | Our Implementation |
|--------|----------------------|-------------------|
| Source data | CSW geospatial metadata | LLMDataHub + CADMIES |
| Custom Lexicon | Not applicable (uses core schema only) | `project-hierion.llmdatahub` and `project-hierion.cadmies` |
| Deployment | GitHub Actions | Manual + future GitHub Actions |

## Lessons Learned

1. **GitHub Actions is the target deployment model.** vmx's reference implementation proves this works at scale.

2. **Rate limit spreading is essential.** The pattern of checking headers and delaying between publishes is proven.

3. **Custom Lexicons are our unique addition.** We're building on the foundation, not just replicating it.

## Next Steps

1. Design GitHub Actions workflow for automated publishing
2. Test with bulk dry runs before live publishing
3. Monitor rate limit headers during bulk operations

## References

- [gdi-de-csw-to-atproto](https://github.com/vmx/gdi-de-csw-to-atproto)
- [AT Protocol Rate Limits](https://docs.bsky.app/docs/advanced-guides/rate-limits)
- [Matadisco GitHub](https://github.com/vmx/matadisco)

---

*Let the mycelium grow!*
