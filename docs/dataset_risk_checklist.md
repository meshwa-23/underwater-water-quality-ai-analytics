# Dataset Risk Checklist

## 1. Missing-Data Risks

| Risk | What to Check | Impact |
|---|---|---|
| Missing measurements | Percentage of missing values per column | Reduced training data |
| Consecutive missing periods | Long gaps in time series | Breaks temporal continuity |
| Missing timestamps | Gaps in time sequence | Incorrect temporal features |
| Sensor dropout | Sudden periods with no measurements | False patterns/anomalies |
| Missing target values | Missing forecasting target | Cannot calculate training loss/metrics |

Status: To be assessed after dataset inspection.

---

## 2. Annotation Risks

| Risk | What to Check | Impact |
|---|---|---|
| No anomaly labels | Check whether labels exist | Requires unsupervised detection |
| Inconsistent labels | Compare annotation rules | Unreliable evaluation |
| Subjective labels | Understand who/what created labels | Possible label bias |
| Sparse anomaly labels | Count anomaly vs normal observations | Poor supervised learning |
| Unknown anomaly definition | Confirm domain definition | Evaluation ambiguity |

Status: To be confirmed.

---

## 3. Class Imbalance Risks

Relevant mainly if anomaly labels are available.

Check:

- Number of normal observations
- Number of anomalous observations
- Percentage of each class
- Number of anomalies per time period
- Number of anomalies per sensor/location

Potential issue:

```text
Normal observations >>> Anomalous observations