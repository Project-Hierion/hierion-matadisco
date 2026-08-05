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

Core Field Definitions
Field	Type	Required	Description
resource	string	Yes	URI pointing to the dataset (Hugging Face, GitHub, or other repository)
publishedAt	string	Yes	Date the dataset was published (ISO format YYYY-MM-DD)
tags	array	No	Max 20 tags, each 1-200 characters. Must include project-hierion plus dataset-specific tags
preview	object	No	Preview link with mimeType and URL for quick reference
Custom Top-Level Key: project-hierion
All Project Hierion metadata lives under the project-hierion key. This key must match the project-hierion tag in the tags array.

$type Field
Records published to Matadisco require two $type fields:

Top-level $type — Always cx.vmx.matadisco. This identifies the record as a Matadisco record to the network.

Custom $type — Inside your custom key (project-hierion), use your Lexicon ID (project-hierion.llmdatahub). This identifies the structure of your custom data.

Schema Structure
json
{
  "project-hierion": {
    "$type": "project-hierion.llmdatahub",
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
Field Definitions
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
License Policy
Only datasets with explicit open licenses are published:

MIT

Apache 2.0

CC-BY (any version)

BSD (any version)

GPL (any version)

Datasets with no license, unclear licensing, or restrictive terms are skipped.

Tagging Guidelines
Required tags:

project-hierion — always included

Recommended tags:

Dataset name (e.g., dolphin, ultrachat)

Category (e.g., instruction-tuning, pretraining, sft)

Domain (e.g., text-generation, conversation)

Example Record
json
{
  "$type": "cx.vmx.matadisco",
  "resource": "https://huggingface.co/datasets/QuixiAI/dolphin",
  "publishedAt": "2023-07-01",
  "tags": ["project-hierion", "dolphin", "instruction-tuning", "sft", "text-generation"],
  "preview": {
    "mimeType": "text/html",
    "url": "https://huggingface.co/datasets/QuixiAI/dolphin"
  },
  "project-hierion": {
    "$type": "project-hierion.llmdatahub",
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
Version History
Date	Version	Changes
2026-07-31	1.0	Initial schema definition
2026-08-05	1.1	Added $type field documentation and corrected example
