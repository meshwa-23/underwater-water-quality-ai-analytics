# Reproducible Pipeline Flowchart

```text
                RAW DATASET
                     │
                     ▼
          ┌─────────────────────┐
          │ Data Validation     │
          │ • columns           │
          │ • types             │
          │ • timestamps        │
          │ • units             │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Data Cleaning       │
          │ • missing values    │
          │ • duplicates        │
          │ • invalid values    │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Exploratory         │
          │ Data Analysis       │
          │ • trends            │
          │ • distributions     │
          │ • correlations      │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Temporal Processing │
          │ • sort by time      │
          │ • sampling check    │
          │ • lag features      │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Temporal Split      │
          │ Train / Validation  │
          │ / Test              │
          └──────────┬──────────┘
                     │
             ┌───────┴────────┐
             ▼                ▼
   ┌─────────────────┐  ┌─────────────────┐
   │ Anomaly         │  │ Forecasting     │
   │ Detection       │  │                 │
   └────────┬────────┘  └────────┬────────┘
            │                    │
            ▼                    ▼
   Statistical Baseline   Persistence /
            │             Linear Regression
            ▼                    │
     Isolation Forest            ▼
            │             Random Forest
            │                    │
            │                    ▼
            │                XGBoost
            │                    │
            └─────────┬──────────┘
                      ▼
             MODEL EVALUATION
                      │
                      ▼
             MODEL COMPARISON
                      │
                      ▼
             FINAL RESULTS
                      │
                      ▼
             VISUALIZATION
                      │
                      ▼
              FINAL REPORT