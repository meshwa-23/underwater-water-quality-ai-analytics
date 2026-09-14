# Mentor Corrections — Methodology V1

## Purpose

This document records mentor feedback and the changes made to Methodology V1.

No decision should be marked as approved unless it has actually been confirmed by the mentor.

---

## 1. Research Question

### V1

How can time-stamped underwater water-quality measurements be used to detect anomalous environmental conditions and forecast future water-quality parameters using machine learning?

### Mentor Feedback

-

### Correction Made

-

---

## 2. Anomaly Target

### Proposed Definition

An anomaly is an observation or period that significantly deviates from expected environmental behaviour.

### Mentor Feedback

-

### Final Decision

-



## 3. Forecasting Target

- Temperature
### Proposed Targets

- pH
- Dissolved oxygen
- Pressure
- Other available parameters

### Mentor Feedback

-

### Final Target

-

---

## 4. Forecast Horizon

### Proposed

To be determined after confirming sampling frequency.

### Mentor Feedback

-

### Final Decision

-

---

## 5. Train / Validation / Test Split

### Proposed

70% Train  
15% Validation  
15% Test

Chronological split without random shuffling.

### Mentor Feedback

-

### Final Decision

-

---

## 6. Evaluation Metrics

### Anomaly Detection

Proposed:

- Precision
- Recall
- F1-score
- PR-AUC where appropriate
- Detection rate when labels are unavailable

### Forecasting

Proposed:

- MAE
- RMSE
- R²
- MAPE where appropriate

### Processing

- Training time
- Prediction time
- Total processing time

### Mentor Feedback

-

### Final Decision

-

---

## 7. Modelling Constraints

### Proposed

- Statistical baseline required
- Isolation Forest as primary anomaly model
- Random Forest/XGBoost for forecasting
- Sequence model only if justified
- No hardware deployment
- No on-device ML

### Mentor Feedback

-

### Final Decision

-

---

## 8. Changes to Methodology V1

| Area               | V1            | Mentor Correction | Updated Version |
| ------------------ | ------------- | ----------------- | --------------- |
| Anomaly definition | TBD           | TBD               | TBD             |
| Forecast target    | TBD           | TBD               | TBD             |
| Forecast horizon   | TBD           | TBD               | TBD             |
| Data split         | 70/15/15      | TBD               | TBD             |
| Metrics            | MAE/RMSE etc. | TBD               | TBD             |
| Models             | Baseline + ML | TBD               | TBD             |

---

## 9. Final Confirmed Decisions

After the mentor review, record only confirmed decisions here.

1.
2.
3.
4.
5.

---

## 10. Updated Assumptions

1.
2.
3.
