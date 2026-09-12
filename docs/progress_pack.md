# Individual Progress Pack — Week 1

## Slide 1 — Completed Work

### Problem Understanding
- Defined the project as a software-based AI/ML system for underwater environmental time-series analysis.
- Identified two major tasks:
  - Anomaly detection
  - Future water-quality forecasting

### Data Understanding
Expected inputs include:
- Timestamp
- Temperature
- pH
- Dissolved Oxygen
- Pressure
- Other available water-quality variables

### Research Completed
Reviewed related work covering:
- AI/ML for water-quality monitoring
- IoT-based water-quality analytics
- Anomaly detection
- Dissolved oxygen prediction
- Tree-based forecasting
- Deep learning for time-series forecasting

---

## Slide 2 — Findings, Blockers and Research Framing

### Key Findings

- Water-quality measurements are naturally treated as time-series data.
- Temperature can be an important predictor of dissolved oxygen.
- Tree-based models such as Random Forest and XGBoost are strong candidates for nonlinear relationships.
- Statistical anomaly detection provides an important baseline.
- Isolation Forest is a suitable candidate for unsupervised anomaly detection.
- Deep sequence models should only be considered if the dataset has sufficient temporal coverage.

### Current Blockers / Unknowns

- Exact dataset structure is not yet confirmed.
- Sampling frequency needs to be determined.
- Missing-value pattern needs to be analyzed.
- Units and valid ranges need confirmation.
- Availability of anomaly labels is unknown.
- Forecast horizon needs to be finalized.
- Exact target parameter(s) for forecasting need mentor confirmation.

### Revised Research Question

How can time-stamped underwater water-quality measurements be used to detect anomalous environmental conditions and forecast future water-quality parameters using machine learning?

---

## Slide 3 — Next Plan and Mentor Confirmation

### Mentor Confirmation Required

1. Confirm exact target parameters for forecasting.
2. Confirm definition of an anomaly.
3. Confirm whether anomaly labels are available.
4. Confirm required forecast horizon.
5. Confirm evaluation metrics.
6. Confirm dataset sampling frequency and temporal resolution.
7. Confirm whether all available variables should be used as model features.
8. Confirm final project scope.

### Next Plan

1. Obtain and inspect the dataset.
2. Analyze dataset structure and temporal coverage.
3. Check missing values, duplicates and irregular timestamps.
4. Verify units, ranges and data quality.
5. Perform exploratory time-series analysis.
6. Establish statistical anomaly baseline.
7. Establish forecasting baseline.
8. Compare candidate models after data understanding is complete.

### Expected Next Deliverable

Dataset analysis + validated target definition + experimental plan.