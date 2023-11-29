# FARM Stack Template
This is a template I built for learning purposed. 
It is supposed to be used as a backend of a FARM stack (FastAPI, React, MongoDB).
It uses beanie as a ORM mapper and pydantic-settings to read environment variables.

## Setup
In the following I have written down the steps to setup and run this stack on a Linux machine
```bash
# Copy .env.example file to .env (modify values if required)
cp .env.example .env

# Setup virtualenv
python3 -m venv venv

# Activate virtualenv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run MongoDB container
docker compose up -d

# Run FastAPI server
# (omit "--reload" for prod server)
uvicorn app.main:app --reload
```