# End-to-End Software Pipeline

```text
┌──────────────────────────────────────┐
│ Timestamped Water-Quality Data       │
│                                      │
│ Temperature | pH | DO | Pressure     │
│ + Other Environmental Variables      │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ Data Ingestion                        │
│ Load dataset and inspect structure    │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ Data Validation & Cleaning            │
│ Missing values | Duplicates | Errors  │
│ Timestamp validation | Outliers       │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ Exploratory Data Analysis             │
│ Trends | Seasonality | Correlations   │
│ Distributions | Temporal patterns     │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ Time-Series Preparation               │
│ Sorting | Resampling | Windowing      │
│ Train/Validation/Test split           │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ Feature Engineering                   │
│ Lag features | Rolling statistics     │
│ Temporal features | Derived variables │
└──────────────────┬───────────────────┘
                   │
          ┌────────┴────────┐
          ▼                 ▼
┌───────────────────┐ ┌───────────────────┐
│ Anomaly Detection │ │   Forecasting     │
│                   │ │                   │
│ Detect unusual    │ │ Predict future    │
│ observations      │ │ parameter values  │
└─────────┬─────────┘ └─────────┬─────────┘
          │                     │
          ▼                     ▼
┌───────────────────┐ ┌───────────────────┐
│ Anomaly Flags     │ │ Future Values     │
│ Anomaly Scores    │ │ Prediction Error  │
└─────────┬─────────┘ └─────────┬─────────┘
          │                     │
          └──────────┬──────────┘
                     ▼
        ┌──────────────────────────┐
        │ Model Evaluation         │
        │ Metrics | Validation     │
        │ Error Analysis           │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │ Results & Visualization  │
        │ Charts | Tables | Insights│
        └──────────────────────────┘