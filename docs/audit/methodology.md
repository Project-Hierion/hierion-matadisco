# License Audit Methodology

## Purpose

This document defines the methodology used to audit datasets in the LLMDataHub fork for license compliance and eligibility for publication to Matadisco.

## Audit Criteria

A dataset is eligible for publication if it meets all of the following criteria:

1. **Explicit open license** — The dataset must include a clear, unambiguous license statement. Acceptable licenses:
   - MIT
   - Apache 2.0
   - CC-BY (any version)
   - BSD (any version)
   - GPL (any version)
   - Any OSI-approved open license

2. **License location** — The license must be found in one of these locations (in order of preference):
   - Dataset repository (LICENSE file, README, or dataset card)
   - Official dataset documentation
   - Original publication or paper
   - Explicit statement from the author/organization

3. **Attribution available** — The dataset must include or reference the original authors/creators.

## Exclusion Criteria

A dataset is **ineligible** for publication if any of these apply:

1. **No license specified** — If the license is not explicitly stated anywhere
2. **Unclear license** — If the license is ambiguous, contradictory, or uses non-standard terminology
3. **Restrictive license** — Examples include:
   - CC BY-NC (non-commercial only)
   - CC BY-ND (no derivatives)
   - Custom restrictive terms
   - Research-only licenses
4. **License unknown** — If the dataset is from a source where license status cannot be verified

## Audit Process

### Step 1: Identify Dataset Source

- Determine the primary source of the dataset (Hugging Face, GitHub, institutional site, etc.)
- Record the source URL in the audit log

### Step 2: Search for License

Check these locations in order:

1. Repository root: `LICENSE`, `LICENSE.txt`, `LICENSE.md`
2. Dataset card or README: Look for "License", "Licensing", "Terms of Use" section
3. Model card or documentation: Similar to dataset card
4. Original paper: Check for license statement or Terms of Use
5. Author/organization website: Check for dataset licensing page

### Step 3: Verify License

- Confirm the license is one of the accepted open licenses
- Ensure the license matches the official text of that license
- Check if there are any additional terms or restrictions

### Step 4: Document

Record the following in the audit log:
- Dataset name
- License
- License source (where it was found)
- Date verified
- Status (PASS or SKIP)
- Notes (any clarifying information)

### Step 5: Attribution

- Document the author(s) or organization responsible for the dataset
- Include any citation requirements

## Verification Sources

| Source | Priority | Reliability |
|--------|----------|-------------|
| Official repository (GitHub, Hugging Face, etc.) | 1 | High |
| Dataset card or README | 2 | High |
| Original publication or paper | 3 | Medium |
| Author/organization website | 4 | Medium |
| Third-party references | 5 | Low |

## Audit Log Format

Each dataset entry in `license-audit.md` should follow this format:

| Dataset | License | Status | Notes |
|---------|---------|--------|-------|
| dataset-name | MIT | ✅ PASS | Verified in README. Author: Author Name. |

## Notes on Specific Licenses

| License |	Acronym | Eligibility | Notes
|---------|---------|--------|-------|
MIT	| MIT	| ✅	| Permissive, widely used
Apache 2.0	| Apache	| ✅	| Permissive with patent grant
Creative Commons Attribution	| CC BY	| ✅	| All versions accepted
Creative Commons Non-Commercial	| CC BY-NC	| ❌	| Non-commercial restriction
Creative Commons No Derivatives	| CC BY-ND	| ❌	| No derivatives restriction
BSD 2-Clause/3-Clause	| BSD	| ✅	| Permissive
GNU General Public License	| GPL	| ✅	| Copyleft, acceptable
Research Only	| N/A	| ❌	| Too restrictive for publishing

## Version History

| Date |	Version |	Changes
|---------|---------|--------|
| 2026-07-31	| 1.0	| Initial methodology definition
