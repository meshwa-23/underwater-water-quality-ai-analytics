# Experiment Plan V2

## 1. Confirmed Experimental Structure

The project will compare simple baselines against machine-learning methods using the same temporal dataset split.

Two experimental tracks will be maintained:

1. Anomaly Detection
2. Forecasting

---

# 2. Experiment Track A — Anomaly Detection

## Baseline

Statistical methods:

- Rolling Z-score
- IQR / MAD

## Primary ML Method

- Isolation Forest

## Optional Method

- Local Outlier Factor

## Evaluation

### If labels exist

- Precision
- Recall
- F1-score
- Confusion matrix
- PR-AUC where appropriate

### If labels do not exist

- Number of anomalies detected
- Anomaly detection rate
- Anomaly score distribution
- Temporal consistency
- Visual inspection
- Domain validation

---

# 3. Experiment Track B — Forecasting

## Baselines

1. Persistence
2. Moving average
3. Linear Regression

## Advanced Models

1. Random Forest Regression
2. XGBoost Regression

## Optional Sequence Model

- LSTM
- GRU

These will only be considered if the dataset provides enough temporal observations and the simpler models justify further investigation.

---

# 4. Data Split

The default strategy is chronological splitting.

Initial proposal:

- 70% Train
- 15% Validation
- 15% Test

No random shuffling of the full time series.

The final split will be confirmed with the mentor after the dataset is inspected.

---

# 5. Forecast Horizon

The forecast horizon will be determined after confirming:

- Sampling frequency
- Temporal coverage
- Project requirements
- Mentor guidance

The horizon will not be arbitrarily selected before understanding the dataset.

---

# 6. Feature Engineering

Potential features:

- Current environmental measurements
- Lag features
- Rolling statistics
- Calendar/time features
- Sensor/location metadata where appropriate

No feature may use information occurring after the prediction timestamp.

---

# 7. Evaluation Criteria

| Task | Primary Metrics | Secondary Metrics |
|---|---|---|
| Anomaly Detection with labels | Precision, Recall, F1 | PR-AUC, confusion matrix |
| Anomaly Detection without labels | Detection rate, anomaly scores | Visual/domain validation |
| Forecasting | MAE, RMSE | R², MAPE |
| Processing | Total processing time | Training/prediction time |

---

# 8. Constraints

The project is:

- Software-only
- Individual
- Focused on historical time-series data
- Not intended for hardware development
- Not intended for on-device deployment

The final model must be justified using experimental evidence rather than model complexity alone.

---

# 9. Final Model Selection

The final method will be selected using:

1. Evaluation performance
2. Generalization on unseen test data
3. Robustness
4. Interpretability
5. Processing time
6. Suitability for the dataset

---

# 10. Pending Mentor Confirmation

- [ ] Exact forecasting target
- [ ] Forecast horizon
- [ ] Anomaly definition
- [ ] Availability of anomaly labels
- [ ] Train/validation/test percentages
- [ ] Final evaluation metrics
- [ ] Whether optional models are required