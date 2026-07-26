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
```bash
uvicorn src.api:app --reload
```

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

### Endpoints
- `GET /` — health check / welcome message
- `POST /greet` — simple greeting, takes `{"name": "..."}`
- `POST /passenger-summary` — validates and echoes passenger info
- `POST /predict` — predicts Titanic survival given `{"age": ..., "fare": ..., "pclass": ...}`, returns prediction + probability

## Model
A logistic regression model is trained via:
```bash
python -m src.train
```
This saves `model.joblib`, which the API loads at startup.

# Titanic Survival Predictor — ML Engineering Practice Project

A small end-to-end project demonstrating core software/ML engineering practices: 
modular code, centralized logging, automated testing, and a served ML model via a REST API.

Built as a learning project transitioning from notebook-based data science to 
production-style ML engineering.

## What it does
Trains a logistic regression model to predict Titanic passenger survival based on 
age, fare, and passenger class, and serves predictions through a FastAPI endpoint.

## Project structure
- `src/data.py` — data loading and summarization logic
- `src/train.py` — model training script
- `src/api.py` — FastAPI application serving predictions
- `src/logger_config.py` — centralized logging configuration used across all modules
- `tests/` — pytest test suite covering data logic and API behavior (12 tests)
- `model.joblib` — trained model artifact

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Train the model

```bash
python -m src.train
```

## Run the API

```bash
uvicorn src.api:app --reload
```

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

## API Endpoints
- `GET /` — health check
- `POST /predict` — predicts survival given passenger details

Example request:
```json
{
  "age": 29,
  "fare": 100,
  "pclass": 1
}
```

Example response:
```json
{
  "survived_prediction": 1,
  "survival_probability": 0.928
}
```

Input is validated: `pclass` must be 1, 2, or 3; `age` must be between 0 and 120; 
`fare` must be non-negative.

## Run tests

```bash
pytest --cov=src --cov-report=term-missing
```

## Tools & practices used
- `pytest` + `pytest-cov` for testing and coverage
- `black` + `ruff` for formatting and linting
- Centralized logging (not per-file `basicConfig` calls)
- Input validation via Pydantic models + custom business-rule checks
- Git workflow: feature branches, pull requests, resolved a real merge conflict