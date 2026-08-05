# SOP — License Audit for Matadisco Publishing

## Purpose

This document defines the standard operating procedure for auditing dataset licenses before publishing to Matadisco. Only datasets with explicit open licenses are eligible for publication.

## Scope

This SOP covers:
- Identifying dataset sources
- Locating and verifying license information
- Documenting audit results
- Making pass/skip decisions
- Maintaining audit records

## Prerequisites

Before starting an audit, ensure:

- [ ] Dataset source URL is known
- [ ] Dataset is in the LLMDataHub fork
- [ ] Access to the dataset's repository or documentation

## Audit Criteria

### Pass Criteria

A dataset passes the audit if it has **one or more** of these licenses:
- MIT
- Apache 2.0
- CC-BY (any version)
- BSD (any version)
- GPL (any version)
- Any OSI-approved open license

### Skip Criteria

A dataset is skipped if:
- No license is specified or findable
- License is unclear or ambiguous
- License is restrictive (e.g., CC BY-NC, research-only)
- License uses non-standard terms that don't clearly grant open use

## Audit Workflow

### Step 1: Identify Dataset Source

1. Locate the dataset in the LLMDataHub fork
2. Record the primary source URL:
   - Hugging Face dataset page
   - GitHub repository
   - Institutional website
   - Original publication

### Step 2: Search for License Information

Check these locations in order:

| Priority | Location | What to look for |
|----------|----------|------------------|
| 1 | Repository root | `LICENSE`, `LICENSE.txt`, `LICENSE.md` |
| 2 | Dataset card or README | "License", "Licensing", "Terms of Use" section |
| 3 | Model card or documentation | Similar to dataset card |
| 4 | Original paper | License statement or Terms of Use |
| 5 | Author/organization website | Dataset licensing page |

### Step 3: Verify License

1. Confirm the license is one of the accepted open licenses
2. Ensure the license matches the official text of that license
3. Check for additional terms or restrictions
4. If license is found in multiple places, verify they match

### Step 4: Document Audit Results

Add an entry to the audit log:

```markdown
| Dataset | License | Status | Notes |
|---------|---------|--------|-------|
| dataset-name | MIT | ✅ PASS | Verified in README. Author: Author Name. |
```

Step 5: Attribution
Record the author(s) or organization responsible for the dataset

Note any citation requirements

Add to attribution field in the record

Audit Log Format
Maintain a comprehensive audit log in docs/audit/license-audit.md:

markdown
# LLMDataHub License Audit

## Audit Status

| Dataset | License | Status | Notes |
|---------|---------|--------|-------|
| dolphin | MIT | ✅ PASS | QuixiAI/Eric Hartford. Verified in README. |
| ultrachat | MIT | ✅ PASS | Verified in dataset card. |
| ... | ... | ... | ... |

## Audit Log

| Date | Dataset | Action | Notes |
|------|---------|--------|-------|
| 2026-07-31 | dolphin | ✅ PASS | MIT license verified |
| 2026-07-31 | ultrachat | ✅ PASS | MIT license verified |
Verification Checklist
For each dataset, verify:

□ License is explicitly stated
□ License is open (permissive or copyleft)
□ License source is documented
□ Author/organization is credited
□ Any citation requirements are noted
□ Audit log is updated

Notes on Specific Licenses
License	Acronym	Eligibility	Notes
MIT	MIT	✅ PASS	Permissive, widely used
Apache 2.0	Apache	✅ PASS	Permissive with patent grant
Creative Commons Attribution	CC BY	✅ PASS	All versions accepted
Creative Commons Non-Commercial	CC BY-NC	❌ SKIP	Non-commercial restriction
Creative Commons No Derivatives	CC BY-ND	❌ SKIP	No derivatives restriction
BSD 2-Clause/3-Clause	BSD	✅ PASS	Permissive
GNU General Public License	GPL	✅ PASS	Copyleft, acceptable
Research Only	N/A	❌ SKIP	Too restrictive for publishing

Version History
Date	Version	Changes
2026-08-05	1.0	Initial SOP definition
