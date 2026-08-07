# AT Protocol Rate Limits — Strategy Documentation

## Purpose

This document documents the rate limit system for the AT Protocol and defines our strategy for publishing records to Matadisco without hitting limits.

## Overview

AT Protocol enforces rate limits at multiple layers to ensure service stability and prevent abuse. Limits apply to:

- **Content write operations** (publishing records) — points-based system per account
- **General API requests** — throttled per IP address
- **Specific sensitive operations** — tighter limits (account creation, session creation, handle updates)
- **Relay (firehose) consumption** — for PDS instances

## Content Write Limits (Our Primary Concern)

Publishing records to Matadisco uses `com.atproto.repo.createRecord` operations. These are rate-limited using a **points-based system** per account (DID):
```text
| Action | Points | Description |
|--------|--------|-------------|
| CREATE | 3 points | New record creation (our main operation) |
| UPDATE | 2 points | Modifying existing records |
| DELETE | 1 point | Removing records |
```

**Quotas per account:**
```text
| Time Window | Points Limit | Max Records (CREATE) |
|-------------|--------------|---------------------|
| Per Hour | 5,000 points | ~1,666 records/hour |
| Per Day | 35,000 points | ~11,666 records/day |
```

**Our publishing capacity:**
- Hourly: ~1,666 records
- Daily: ~11,666 records

For our 636 CADMIES concepts + LLMDataHub datasets, we can publish everything in under an hour with proper spreading.

## General API Request Limits

Most authenticated API requests are limited by IP address:
```text
| Limit | Value |
|-------|-------|
| Requests per 5 minutes | 3,000 per IP |
```

## Authentication Limits

Login operations have stricter limits:
```text
| Operation | Limit |
|-----------|-------|
| Session creation (`createSession`) | 30 per 5 minutes, 300 per day per account |
| Account creation | 100 per 5 minutes per IP |
```

**Strategy:** Authenticate once per session and reuse the session. Do not call login repeatedly.

## Rate Limit Headers

AT Protocol servers advertise rate limit state on **every response** (not just 429s) via HTTP headers:
```text
| Header | Description |
|--------|-------------|
| `ratelimit-limit` | Request ceiling for the current window |
| `ratelimit-remaining` | Requests left in the current window |
| `ratelimit-reset` | Unix timestamp (seconds) when the window resets |
| `ratelimit-policy` | Server's opaque policy descriptor |
```

**Key insight:** These headers let you pace yourself *before* hitting a 429 response.

## Our Publishing Strategy

### 1. Authenticate Once, Reuse Session

```python
# DO: Authenticate once, keep client alive
client = create_client(pds_url)
session = client.login(handle, app_password)

# DO: Reuse the session for all publishes
for record in records:
    client.publish(record, session=session)

# DO NOT: Call login() before every publish
```

This avoids hitting the session creation rate limits.

### 2. Monitor Rate Limit Headers
   
Check headers after each publish:

```python
def check_rate_limits(response):
    remaining = response.headers.get('ratelimit-remaining')
    if remaining and int(remaining) < 10:
        # Slow down, we're close to the limit
        time.sleep(calculate_backoff(response))
```

### 3. Spread Publishing Over Time

For bulk publishing, spread records across the hour:

```python
def publish_with_spreading(records):
    for i, record in enumerate(records):
        publish(record)
        # Calculate delay based on remaining quota
        delay = calculate_delay(i, len(records))
        time.sleep(delay)
```

Delay calculation: If we have 636 records and 1 hour (3,600 seconds):

Average delay: 3,600 / 636 ≈ 5.6 seconds

Recommended: use --spread flag with 1-5 second delays

### 4. Handle 429 Responses Gracefully
 
If we hit a rate limit:

```python
def handle_rate_limit(response):
    if response.status_code == 429:
        reset_time = int(response.headers.get('ratelimit-reset', 0))
        wait_seconds = max(reset_time - time.time(), 1)
        time.sleep(wait_seconds)
        # Retry
```

## Reference Implementation

The gdi-de-csw-to-atproto repo handles spikes by spreading out publishes. Key pattern:

Check ratelimit-remaining on each response

If remaining is low, delay before next publish

If 429 is hit, wait until ratelimit-reset

Relay Limits (Self-Hosted PDS)

If we self-host a PDS, we must also respect relay limits:
```text
Limit	Value
Repository stream events (per second)	50/sec
Repository stream events (per hour)	2,600/hour
Repository stream events (per day)	21,000/day
Account capacity per PDS	100 accounts max
Accounts created per second	5/sec
```

Our situation: We're publishing to our own PDS, which is connected to the AT Protocol network. These limits apply to how fast we can publish records.

## Environment Variables

Our .env.example includes rate limit configuration:

```bash
# Rate Limit Configuration
MATADISCO_MIN_DELAY=1.0
MATADISCO_MAX_DELAY=5.0
```

Recommendation for bulk publishing:

- Start with MIN_DELAY=2.0, MAX_DELAY=8.0

- Monitor headers and adjust

##  Publish Test Results

During our Phase 73C testing, we observed the following rate limit behavior:
```text
Test	Records Published	Rate Limit Remaining	Reset
Initial publish (Dolphin)	1	2997	1785961348
Publish (Anatta)	1	2995	1785961348
Publish (Interconnectedness)	1	2993	1785961348
Re-publish (Dolphin)	1	2998	1786084157
Re-publish (Anatta)	1	2996	1786084157
Re-publish (Interconnectedness)	1	2994	1786084157
```

Each publish consumed 3 points. With a limit of 5,000 points per hour, we have room for ~1,666 publishes per hour.

## Key Observation: 

Rate limit headers report remaining points, not remaining requests. Each CREATE uses 3 points, so the ratelimit-remaining value decreases by 3 per publish.

Summary
```text
Limit Type	Our Strategy
Write points (hourly)	Spread 636 concepts over 1 hour (~5.6s delay each)
Write points (daily)	Well below 35,000 limit
General API requests	Low volume, well below 3,000/5min
Session creation	Login once, reuse session
Rate limit headers	Monitor and back off if needed
429 responses	Wait for reset and retry
```

## Bottom line: Our 636 concepts + datasets can be published in under an hour with proper spreading. We'll monitor headers and adjust delays as needed.

Version History
```text
Date	Version	Changes
2026-08-05	1.0	Initial rate limits documentation
2026-08-07	1.1	Added publish test results and real-world rate limit data
```
