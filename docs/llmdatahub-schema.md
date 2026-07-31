# LLMDataHub Dataset Schema — Matadisco Records

## Overview

This document defines the schema for publishing LLMDataHub dataset metadata to the Matadisco decentralized data discovery network. Records follow the core `cx.vmx.matadisco` schema with custom metadata under the `project-hierion` top-level key.

## Core Schema

All records must include the core fields defined by the Matadisco lexicon:

```json
{
  "resource": "URI string",
  "publishedAt": "YYYY-MM-DD",
  "tags": ["array", "of", "strings"],
  "preview": {
    "mimeType": "string",
    "url": "URI string"
  }
}
```

## Core Field Definitions
```
Field	Type	Required	Description
resource	string	Yes	URI pointing to the dataset (Hugging Face, GitHub, or other repository)
publishedAt	string	Yes	Date the dataset was published (ISO format YYYY-MM-DD)
tags	array	No	Max 20 tags, each 1-200 characters. Must include project-hierion plus dataset-specific tags
preview	object	No	Preview link with mimeType and URL for quick reference
```

## Custom Top-Level Key: project-hierion

All Project Hierion metadata lives under the project-hierion key. This key must match the project-hierion tag in the tags array.

## Schema Structure
```
{
  "project-hierion": {
    "datasetName": "string",
    "organization": "string",
    "authors": ["string"],
    "license": "string",
    "description": "string",
    "source": "URI",
    "originalRepo": "URI",
    "size": "string",
    "language": "string",
    "format": "string",
    "attribution": "string",
    "sourceDate": "string (with disclaimer)"
  }
}
```
## Field Definitions
```
Field	Type	Required	Description
datasetName	string	Yes	Short name of the dataset (e.g., "dolphin", "ultrachat")
organization	string	Yes	Organization that published the original dataset
authors	array	Yes	List of individual authors/creators
license	string	Yes	Open license (MIT, Apache, CC-BY, etc.)
description	string	Yes	Brief description of the dataset and its purpose
source	URI	Yes	Direct link to the dataset (same as resource field)
originalRepo	URI	Yes	Link to the original LLMDataHub repository
size	string	No	Approximate size of the dataset (rows, GB, etc.)
language	string	No	Primary language of the dataset
format	string	No	Data format (jsonl, parquet, csv, etc.)
attribution	string	Yes	Full attribution statement with credit to original creators
sourceDate	string	Yes	Date the dataset was sourced, with disclaimer if approximate
```

## License Policy

Only datasets with explicit open licenses are published:

-MIT

- Apache 2.0

- CC-BY (any version)

- BSD (any version)

- GPL (any version)

Datasets with no license, unclear licensing, or restrictive terms are skipped.

## Tagging Guidelines

Required tags:

p- roject-hierion — always included

Recommended tags:

- Dataset name (e.g., dolphin, ultrachat)

- Category (e.g., instruction-tuning, pretraining, sft)

- License (e.g., mit-license, cc-by-sa)

- Domain (e.g., text-generation, conversation)

## Example Record
```
{
  "resource": "https://huggingface.co/datasets/QuixiAI/dolphin",
  "publishedAt": "2023-07-01",
  "tags": ["project-hierion", "dolphin", "instruction-tuning", "sft", "text-generation", "mit-license"],
  "preview": {
    "mimeType": "text/html",
    "url": "https://huggingface.co/datasets/QuixiAI/dolphin"
  },
  "project-hierion": {
    "datasetName": "dolphin",
    "organization": "QuixiAI",
    "authors": ["Eric Hartford"],
    "license": "MIT",
    "description": "An attempt to replicate Microsoft's Orca — instruction-following dataset with complex explanation traces.",
    "source": "https://huggingface.co/datasets/QuixiAI/dolphin",
    "originalRepo": "https://github.com/Zjh-819/LLMDataHub",
    "size": "~4.5M rows",
    "language": "en",
    "format": "jsonl",
    "attribution": "Original dataset by QuixiAI (Eric Hartford) under MIT License. Sourced from LLMDataHub.",
    "sourceDate": "2023-07-01 (Hugging Face commit date — closest available published date for this dataset)"
  }
}
```

## Version History
```
Date	Version	Changes
2026-07-31	1.0	Initial schema definition
```

```
## docs/schema/cadmies-schema.md

markdown
# CADMIES Concept Schema — Matadisco Records

## Overview

This document defines the schema for publishing CADMIES knowledge graph concepts to the Matadisco decentralized data discovery network. Records follow the core `cx.vmx.matadisco` schema with custom metadata under the `cadmies` top-level key.

## Core Schema

All records must include the core fields defined by the Matadisco lexicon:

json
{
  "resource": "URI or CID string",
  "publishedAt": "YYYY-MM-DD",
  "tags": ["array", "of", "strings"],
  "preview": {
    "mimeType": "string",
    "url": "URI string"
  }
}
```

## Core Field Definitions
```
Field	Type	Required	Description
resource	string	Yes	URI or Permanent CID pointing to the concept (gateway page or content-addressed card)
publishedAt	string	Yes	Date the record was prepared (ISO format YYYY-MM-DD)
tags	array	No	Max 20 tags, each 1-200 characters. Must include cadmies plus concept-specific tags
preview	object	No	Preview link with mimeType and URL for quick reference
```

## Custom Top-Level Key: cadmies

All CADMIES concept metadata lives under the cadmies key. This key must match the cadmies tag in the tags array.

## Schema Structure
```
{
  "cadmies": {
    "conceptName": "string",
    "conceptId": "string (CID or UUID)",
    "definition": "string",
    "coreInsight": "string (optional)",
    "domains": ["string"],
    "source": "URI",
    "attribution": "string",
    "sourceDate": "string (with disclaimer)"
  }
}
```

## Field Definitions
```
Field	Type	Required	Description
conceptName	string	Yes	Display name of the concept
conceptId	string	Yes	Unique identifier (Permanent CID or custom ID)
definition	string	Yes	Concise definition of the concept
coreInsight	string	No	The fundamental insight or key takeaway
domains	array	Yes	Canonical domains the concept belongs to (max 15 domains)
source	URI	Yes	Link to the concept's location (gateway page or raw card)
attribution	string	Yes	Credit statement for the concept source
sourceDate	string	Yes	Date the record was prepared, with disclaimer if approximate
```

## Domains

Concepts are tagged with one or more of the 15 canonical domains:

- Physics

- Philosophy

- Biology

- Mathematics

- Consciousness

- Chemistry

- Ethics

- Computer Science

- Psychology

- Spirituality

-Neuroscience

- Sociology

- Economics

- Ecology

- Medicine

## Tagging Guidelines

Required tags:

- cadmies — always included

Recommended tags:

- Concept name (e.g., anatta, interconnectedness)

- Domains (e.g., philosophy, consciousness, spirituality)

- Category (e.g., buddhism, knowledge-graph)

## Example Record
``` json
{
  "resource": "bafyreicunstgpwqzev3aqplnsgiyftsgr3jqwpgg2wgqrmthytt4fhsb2m",
  "publishedAt": "2026-07-31",
  "tags": ["cadmies", "anatta", "not-self", "buddhism", "philosophy", "consciousness", "spirituality"],
  "preview": {
    "mimeType": "text/html",
    "url": "https://project-hierion.org/#anatta-not-self"
  },
  "cadmies": {
    "conceptName": "Anatta Not Self",
    "conceptId": "bafyreicunstgpwqzev3aqplnsgiyftsgr3jqwpgg2wgqrmthytt4fhsb2m",
    "definition": "The Buddhist concept that there is no permanent, unchanging self or ego; instead, self-identities are dependent on various factors and constantly changing.",
    "coreInsight": "The observation of the observer as a composed, passing phenomenon, further emphasizing the impermanence and interconnectedness of all things.",
    "domains": ["Philosophy", "Consciousness", "Spirituality", "Physics"],
    "source": "https://project-hierion.org/#anatta-not-self",
    "attribution": "Concept from CADMIES. Published by Project Hierion.",
    "sourceDate": "2026-07-31 (record preparation date)"
  }
}
```

## Version History
```
Date	Version	Changes
2026-07-31	1.0	Initial schema definition
```
