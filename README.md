# Hierion-Matadisco

**Project Hierion's Producer for publishing LLMDataHub dataset metadata and CADMIES concepts to the Matadisco decentralized data discovery network (AT Protocol)**

---

## Overview

This repository contains the producer pipeline for publishing two types of records to the [Matadisco](https://github.com/vmx/matadisco) network:

1. **LLMDataHub datasets** — License-audited, fully attributed dataset metadata from our reorganized fork of the LLMDataHub repository
2. **CADMIES concepts** — Knowledge graph concepts (636 total) from the CADMIES project, linked to public gateway concept cards

Matadisco is a decentralized data discovery network built by the IPFS Foundation on AT Protocol (the same protocol Bluesky runs on). It functions as a card catalog for datasets, allowing anyone to publish lightweight records pointing to data resources.

---

## Goals

- Publish clean, license-audited dataset references to Matadisco with full attribution
- Make CADMIES concepts discoverable through the decentralized network
- Establish a reproducible pipeline for future data publishing
- Contribute non-geospatial content to the Matadisco ecosystem as an early adopter

---

## Repository Structure (planned, might change as we go)
```text
hierion-matadisco/
├── docs/
│ ├── README.md # Documentation overview
│ ├── schema/
│ │ ├── llmdatahub-schema.md # Custom schema for dataset records
│ │ └── cadmies-schema.md # Custom schema for concept records
│ ├── audit/
│ │ ├── license-audit.md # Full license audit results
│ │ └── methodology.md # Audit methodology and criteria
│ ├── operations/
│ │ ├── setup.md # Environment setup instructions
│ │ ├── manual-run.md # How to run the producer manually
│ │ └── github-actions.md # GitHub Actions automation (future)
│ ├── records/
│ │ ├── test-dataset.json # Test record: LLMDataHub dataset
│ │ ├── test-concept.json # Test record: CADMIES concept
│ │ └── examples/ # Additional example records
│ ├── research/
│ │ ├── gdi-de-analysis.md # Analysis of gdi-de-csw-to-atproto
│ │ └── rate-limits.md # Rate limit strategy documentation
│ └── experiments/
│ └── YYYY-MM-DD-description.md # R&D session logs
├── scripts/
│ └── matadisco_producer.py # Main producer script
├── data/
│ ├── llmdatahub/ # Dataset metadata from LLMDataHub
│ └── cadmies/ # Concept data from CADMIES
├── tests/
│ └── test_producer.py # Unit tests (future)
├── requirements.txt # Python dependencies
├── .env.example # Environment variables template
├── LICENSE # MIT License
└── README.md # This file
```

---

## Dependencies

- Python 3.10+
- AT Protocol Python SDK (`atproto`)
- python-dotenv (for environment variables)

See `requirements.txt` for full list.

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/project-hierion/hierion-matadisco.git
   cd hierion-matadisco
   ```

2. Create and activate a virtual environment:
    ```bash
    `python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    
4. Copy the environment template and fill in your credentials:
    ```bash
    cp .env.example .env
    ```
    
Edit .env with your PDS endpoint, handle, and app password.

## Usage

Manual Run (for testing)
```bash
python scripts/matadisco_producer.py --record-type dataset --dry-run
python scripts/matadisco_producer.py --record-type concept --dry-run
```

*Remove --dry-run to actually publish.*

Full Audit and Publish
```bash
python scripts/matadisco_producer.py --audit      # Run license audit
python scripts/matadisco_producer.py --publish    # Publish all audited records
```

## License Audit Policy

We only publish datasets with explicit open licenses:

MIT

Apache 2.0

CC-BY (any version)

BSD (any version)

GPL (any version)

Datasets with no license, unclear licensing, or restrictive terms are skipped. Full attribution is always included: authors, sources, and license citations.

## Community & Collaboration

We'll obtain guidance from the Matadisco team as work progresses. 

### Our process:

Design schema

Share with vmx (Matadisco lead) for review

Incorporate feedback

Build test records

Share records for final review

Publish officially

*We're early adopters contributing non-geospatial content to perform trial runs of the network.* **For science! =)**

## Related Repositories

LLMDataHub — Our reorganized fork

CADMIES — Knowledge graph

Matadisco — Decentralized data discovery network

gdi-de-csw-to-atproto — Reference producer

## License

MIT License — see LICENSE for details.

## Acknowledgments

vmx and the IPFS Foundation for building Matadisco

The AT Protocol team for the underlying infrastructure

All dataset authors and contributors — we credit you fully

 🍄
