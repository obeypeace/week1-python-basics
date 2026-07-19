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