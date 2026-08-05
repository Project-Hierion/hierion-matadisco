# CADMIES Concept Schema — Matadisco Records

## Overview

This document defines the schema for publishing CADMIES knowledge graph concepts to the Matadisco decentralized data discovery network. Records follow the core `cx.vmx.matadisco` schema with custom metadata under the `cadmies` top-level key.

## Core Schema

All records must include the core fields defined by the Matadisco lexicon:

```json
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

Core Field Definitions
Field	Type	Required	Description
resource	string	Yes	URI or Permanent CID pointing to the concept (gateway page or content-addressed card)
publishedAt	string	Yes	Date the record was prepared (ISO format YYYY-MM-DD)
tags	array	No	Max 20 tags, each 1-200 characters. Must include cadmies plus concept-specific tags
preview	object	No	Preview link with mimeType and URL for quick reference
Custom Top-Level Key: cadmies
All CADMIES concept metadata lives under the cadmies key. This key must match the cadmies tag in the tags array.

$type Field
Records published to Matadisco require two $type fields:

Top-level $type — Always cx.vmx.matadisco. This identifies the record as a Matadisco record to the network.

Custom $type — Inside your custom key (cadmies), use your Lexicon ID (project-hierion.cadmies). This identifies the structure of your custom data.

Schema Structure
json
{
  "cadmies": {
    "$type": "project-hierion.cadmies",
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
Field Definitions
Field	Type	Required	Description
conceptName	string	Yes	Display name of the concept
conceptId	string	Yes	Unique identifier (Permanent CID or custom ID)
definition	string	Yes	Concise definition of the concept
coreInsight	string	No	The fundamental insight or key takeaway
domains	array	Yes	Canonical domains the concept belongs to (max 15 domains)
source	URI	Yes	Link to the concept's location (gateway page or raw card)
attribution	string	Yes	Credit statement for the concept source
sourceDate	string	Yes	Date the record was prepared, with disclaimer if approximate
Domains
Concepts are tagged with one or more of the 15 canonical domains:

Physics

Philosophy

Biology

Mathematics

Consciousness

Chemistry

Ethics

Computer Science

Psychology

Spirituality

Neuroscience

Sociology

Economics

Ecology

Medicine

Tagging Guidelines
Required tags:

cadmies — always included

Recommended tags:

Concept name (e.g., anatta, interconnectedness)

Domains (e.g., philosophy, consciousness, spirituality)

Category (e.g., buddhism, knowledge-graph)

Example Record
json
{
  "$type": "cx.vmx.matadisco",
  "resource": "ipfs://bafyreicunstgpwqzev3aqplnsgiyftsgr3jqwpgg2wgqrmthytt4fhsb2m",
  "publishedAt": "2026-07-31",
  "tags": ["cadmies", "anatta", "not-self", "buddhism", "philosophy", "consciousness", "spirituality"],
  "preview": {
    "mimeType": "text/html",
    "url": "https://project-hierion.org/#anatta-not-self"
  },
  "cadmies": {
    "$type": "project-hierion.cadmies",
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
Version History
Date	Version	Changes
2026-07-31	1.0	Initial schema definition
2026-08-05	1.1	Added $type field documentation and corrected example
