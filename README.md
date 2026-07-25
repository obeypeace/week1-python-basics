## notes
this project is part of my week 1 AI engineering practise.

# Week 1 — Python Basics

A small project practicing core Python engineering skills: virtual environments, 
modular code, logging, and code style tooling — moving beyond notebooks.

## What it does
Loads the Titanic dataset and prints summary statistics (shape, column types, 
descriptive stats).

## Setup

bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


## Usage

bash
python -m src.main


## Project structure
- `src/main.py` — entry point, orchestrates the pipeline
- `src/data.py` — data loading and summarization logic
- `requirements.txt` — project dependencies
- `data.csv` — Titanic dataset (public sample data)

## Tools used
- `logging` for structured output instead of plain print statements
- `black` for consistent code formatting
- `ruff` for linting

## API

Run the API locally:
\`\`\`bash
uvicorn src.api:app --reload
\`\`\`

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

### Endpoints
- `GET /` — health check / welcome message
- `POST /greet` — simple greeting, takes `{"name": "..."}`
- `POST /passenger-summary` — validates and echoes passenger info
- `POST /predict` — predicts Titanic survival given `{"age": ..., "fare": ..., "pclass": ...}`, returns prediction + probability

## Model
A logistic regression model is trained via:
\`\`\`bash
python -m src.train
\`\`\`
This saves `model.joblib`, which the API loads at startup.