# Methodology V1

## 1. Project Objective

The objective is to develop a software-based AI/ML system that uses time-stamped underwater water-quality measurements to:

1. Detect unusual or anomalous environmental observations.
2. Forecast future water-quality parameter values.

The system will focus on parameters such as temperature, pH, dissolved oxygen, pressure and other available environmental variables.

---

## 2. Overall Methodology

The proposed methodology consists of the following stages:

```text
Raw Dataset
     ↓
Data Validation
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Temporal Processing
     ↓
Train / Validation / Test Split
     ↓
Feature Engineering
     ↓
 ┌───────────────┬────────────────┐
 ↓               ↓
Anomaly       Forecasting
Detection     Future Values
 ↓               ↓
Baseline       Baseline
 ↓               ↓
Isolation      Random Forest
Forest         / XGBoost
 ↓               ↓
Evaluation     Evaluation
 └───────┬───────┘
         ↓
 Model Comparison
         ↓
Final Results