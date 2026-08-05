# Setup — Matadisco Producer Environment

## Purpose

This document provides instructions for setting up the development environment for the Matadisco producer.

## Prerequisites

Before starting, ensure you have:

- [ ] Python 3.10 or higher installed
- [ ] Git installed
- [ ] Access to the `hierion-matadisco` repository
- [ ] ATProto account or PDS credentials (for publishing)

## Environment Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Project-Hierion/hierion-matadisco.git
cd hierion-matadisco
```

Step 2: Create Virtual Environment
bash
python -m venv venv
Activate the virtual environment:

Linux/macOS:

bash
source venv/bin/activate
Windows:

bash
venv\Scripts\activate
Step 3: Install Dependencies
bash
pip install -r requirements.txt
Step 4: Configure Environment Variables
Copy the example environment file:

bash
cp .env.example .env
Edit .env with your credentials:

bash
# AT Protocol Authentication
MATADISCO_PDS_URL=https://bsky.social  # or your self-hosted PDS URL
MATADISCO_HANDLE=your-handle-here       # e.g., project-hierion.org
MATADISCO_APP_PASSWORD=your-app-password-here

# Rate Limit Configuration
MATADISCO_MIN_DELAY=1.0
MATADISCO_MAX_DELAY=5.0

# Dry Run Mode (true/false)
MATADISCO_DRY_RUN=false

# Logging
MATADISCO_LOG_LEVEL=INFO
Step 5: Verify Setup
Run a validation check:

bash
python scripts/matadisco_producer.py --validate --file docs/records/test-dolphin-dataset.json
Expected output:

text
✅ Record validates against Lexicon
Step 6: Test Dry Run
bash
python scripts/matadisco_producer.py --dry-run --file docs/records/test-dolphin-dataset.json
Expected output: Preview of the record that would be published.

Troubleshooting
Issue	Solution
ModuleNotFoundError	Run pip install -r requirements.txt
Authentication failed	Verify MATADISCO_APP_PASSWORD is correct
Rate limit hit	Wait and retry; increase MATADISCO_MIN_DELAY
Invalid Lexicon	Check record fields against Lexicon definition
Next Steps
See Manual Run for publishing instructions

See SOP — Matadisco Publishing for full workflow

Version History
Date	Version	Changes
2026-08-05	1.0	Initial setup documentation
