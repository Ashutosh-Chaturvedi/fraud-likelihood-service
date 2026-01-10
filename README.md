# Fraud Likelihood Service

A production-oriented machine learning service that predicts the likelihood of
fraud for a transaction and converts that probability into an explicit business
decision (ALLOW / REVIEW / BLOCK).

This project focuses on **correct system design, separation of concerns, and
production readiness**, rather than maximizing model complexity.

---

## Problem Statement

Online transactions are vulnerable to fraudulent behavior.  
The goal of this service is to estimate the likelihood of fraud **using only
information available at transaction time** and to translate that likelihood
into a concrete, explainable decision.

This mirrors how real-world fraud systems are built:

- probabilistic predictions
- explicit business rules
- clear failure boundaries

---

## Scope and Non-Goals

### In Scope

- Binary fraud likelihood prediction
- Explicit decision logic (ALLOW / REVIEW / BLOCK)
- API-based inference
- Prediction logging for monitoring and analysis
- Dockerized deployment

### Out of Scope (for now)

- Real-time streaming systems
- Deep learning models
- External fraud or risk providers
- Full-scale MLOps pipelines

---

## Input Features

All input features are assumed to be available at the time of transaction
(no future data leakage).

- `amount` (float): transaction amount  
- `transaction_type` (string): e.g. ONLINE, POS  
- `account_age_days` (int): age of account in days  
- `num_transactions_last_24h` (int): recent activity count  
- `avg_transaction_amount_7d` (float): recent spending baseline  
- `is_international` (bool): cross-border transaction flag  

---

## Output and Decision Logic

The model outputs a fraud probability in the range `[0, 1]`.

This probability is mapped to a business decision:

- `p < 0.3` → **ALLOW**
- `0.3 ≤ p < 0.7` → **REVIEW**
- `p ≥ 0.7` → **BLOCK**

Decision logic is intentionally **separated from the ML model**
to reflect real-world production system design.

---

## High-Level Architecture

### Offline (Training)

- Data preprocessing
- Model training
- Model serialization

### Online (Inference)

- FastAPI service loads model once at startup
- Incoming requests are validated
- Model inference is performed
- Decision logic is applied
- Inputs and outputs are logged to a database

---

## Repository Structure

fraud-likelihood-service/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── schemas.py # Request/response models
│ ├── model.py # Model loading & inference
│ ├── decision.py # Business decision logic
│ ├── database.py # Database connection
│ └── crud.py # Database operations
│
├── ml/
│ ├── train.py # Offline training pipeline
│ ├── preprocess.py
│ └── model.pkl # Serialized model (temporary)
│
├── data/
│ └── sample.csv # Sample / synthetic data
│
├── Dockerfile
├── requirements.txt
└── README.md

---

## Assumptions and Limitations

- Uses simplified features for demonstration purposes
- Model is trained on synthetic or public datasets
- Predictions are probabilistic, not guarantees
- Decision thresholds are illustrative and would require tuning in production

---

## Project Status

**Current Phase:** Phase 0 — Project contract and structure

**Completed:**

- Problem definition
- Input/output schema
- Decision logic
- Repository structure

**Next:**

- Offline model training and evaluation

---

## How to Run

Local setup and Docker instructions will be added
after the API layer is implemented.
