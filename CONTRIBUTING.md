# Contributing to Hierion-Matadisco

Thank you for your interest in contributing to Project Hierion's Matadisco producer! This document provides guidelines for contributing to the repository.

## What This Project Does

This repository contains the producer pipeline for publishing:
- License-audited LLMDataHub dataset metadata to Matadisco
- CADMIES knowledge graph concepts to Matadisco

Matadisco is a decentralized data discovery network built by the IPFS Foundation on AT Protocol.

## Ways to Contribute

### Report Issues
- Open an issue for bugs, feature requests, or questions
- Provide clear steps to reproduce bugs
- Include relevant logs or error messages

### Suggest Improvements
- Schema enhancements
- Additional dataset coverage
- Rate limit handling improvements
- Documentation updates

### Submit Pull Requests
- Fork the repository
- Create a feature branch
- Follow the coding standards below
- Open a PR with a clear description of changes

## Getting Started

1. Read the [README](README.md) for project overview
2. Review the [SOPs](docs/operations/) for publishing workflow
3. Check the [schema documentation](docs/schema/) for record structure
4. Set up your environment using [setup.md](docs/operations/setup.md)

## Coding Standards

### Python
- Use Python 3.10 or higher
- Follow PEP 8 style guidelines
- Use type hints where possible
- Include docstrings for functions and classes
- Keep functions focused and single-purpose

### JSON/Records
- Use 2-space indentation
- Include `$type` field in all records
- Validate against Lexicon before submitting

### Documentation
- Use Markdown for all documentation
- Include file paths in code blocks
- Reference related documents with links

## Testing

Before submitting changes:

1. Validate records against Lexicons:
   ```bash
   python scripts/matadisco_producer.py --validate --file docs/records/your-record.json
   ```

Run dry-run to preview:

bash
python scripts/matadisco_producer.py --dry-run --file docs/records/your-record.json
Ensure no rate limit issues:

bash
python scripts/matadisco_producer.py --publish --file docs/records/your-record.json --spread
License Audit Guidelines
If adding new datasets:

Verify explicit open license (MIT, Apache, CC-BY, BSD, GPL)

Document in docs/audit/license-audit.md

Full attribution to original authors

No license or restrictive license = skip

PR Review Process
All PRs require at least one review

Automated validation runs on push

Address all review comments

Keep PRs focused on a single change

Code of Conduct
Be respectful and inclusive

Focus on constructive feedback

Assume good faith

Help others learn

Questions?
Open an issue or reach out via the Project Hierion contact methods listed in the README.
