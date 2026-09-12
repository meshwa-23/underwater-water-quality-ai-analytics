# Problem Understanding Note

## 1. Problem Statement

The objective of this project is to develop a software-based AI/ML system that analyzes time-stamped underwater water-quality measurements to understand environmental conditions, detect unusual or abnormal behavior, and predict future environmental parameter values.

The dataset consists of historical measurements collected over time. Important water-quality parameters include temperature, pH, dissolved oxygen, pressure, and other related variables available in the dataset.

Because the observations are time-dependent, the temporal order of the measurements must be preserved during data analysis, model development, and evaluation.

The project has two main objectives:

1. Detect anomalous or unusual observations and time periods in the water-quality data.
2. Forecast future values of important environmental parameters using historical observations and available features.

The final system should provide meaningful anomaly indicators and reliable future predictions that can help in monitoring underwater environmental conditions.

---

## 2. Technical Interpretation

This project can be treated as a time-series machine learning problem with two major components:

### A. Anomaly Detection

The system should identify observations or periods where the measured environmental conditions significantly differ from the expected normal behavior.

The output may include:

- Anomaly flag
- Anomaly score
- Timestamp of the anomaly
- Affected water-quality parameter(s)

### B. Time-Series Forecasting

The system should use historical time-dependent measurements to predict future environmental parameter values.

Possible forecasting targets include:

- Temperature
- pH
- Dissolved oxygen
- Pressure
- Other relevant water-quality parameters available in the dataset

The forecasting horizon will be determined after understanding the dataset's sampling frequency and project requirements.

---

## 3. Inputs

The primary inputs to the system are timestamped underwater environmental measurements.

Expected input variables include:

| Input            | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| Timestamp        | Date and time of measurement                                  |
| Temperature      | Water temperature measurement                                 |
| pH               | Acidity/alkalinity measurement                                |
| Dissolved Oxygen | Amount of dissolved oxygen in water                           |
| Pressure         | Underwater pressure measurement                               |
| Other Variables  | Additional available water-quality/environmental measurements |

The exact set of variables, units, sampling frequency, missing values, and data quality will be confirmed during dataset exploration.

---

## 4. Required Outputs

The system should generate two major categories of outputs.

### Anomaly Detection Output

- Anomaly flag
- Anomaly score
- Timestamp associated with the anomaly
- Potentially affected parameter(s)

### Forecasting Output

- Predicted future environmental parameter values
- Corresponding future timestamps
- Forecast evaluation metrics
- Comparison between actual and predicted values

---

## 5. End-to-End System Objective

The complete system should transform raw time-stamped environmental measurements into useful monitoring and prediction results.

The overall process is:

Raw Data
→ Data Validation
→ Data Cleaning
→ Exploratory Data Analysis
→ Time-Series Preparation
→ Feature Engineering
→ Anomaly Detection
→ Forecasting
→ Model Evaluation
→ Results and Visualization

---

## 6. Success Criteria

The project will be considered successful if:

1. The raw dataset is correctly loaded and understood.
2. Timestamp information is correctly parsed and preserved.
3. Missing, duplicate, invalid, or inconsistent observations are identified and handled appropriately.
4. Important temporal patterns and relationships between environmental variables are identified.
5. The anomaly detection component can identify unusual observations or periods and provide interpretable anomaly scores/flags.
6. The forecasting component can predict future environmental parameter values with acceptable error.
7. Models are evaluated using appropriate metrics.
8. Training and testing data are separated chronologically to avoid future-data leakage.
9. Results are visualized clearly using suitable plots and tables.
10. The final system produces reproducible and technically justified results.

---

## 7. Current Assumptions

At the beginning of the project, the following assumptions are made:

- The dataset contains timestamped observations.
- Measurements are collected repeatedly over time.
- Temperature, pH, dissolved oxygen, and pressure are available or expected to be available.
- Additional environmental variables may also be present.
- The problem does not initially provide reliable anomaly labels.
- The temporal order of observations must be preserved.
- Future information should not be used when training models to predict the past or future.
- The appropriate anomaly detection and forecasting algorithms will be selected after exploratory analysis.

These assumptions must be verified after inspecting the actual dataset.

---

## 8. Technical Questions Requiring Clarification

1. What is the exact sampling frequency of the measurements?
2. Are the timestamps equally spaced or irregularly sampled?
3. Which water-quality parameters are actually present in the dataset?
4. What are the units of measurement for each parameter?
5. Are there known or manually labelled anomalies in the dataset?
6. If anomaly labels are unavailable, what definition of "anomaly" should be used?
7. What forecasting horizon is required: minutes, hours, days, or another period?
8. Should the system forecast all available environmental parameters or only selected parameters?
9. How should missing measurements be handled?
10. How should duplicate or invalid sensor readings be treated?
11. Are there multiple sensors or monitoring locations in the dataset?
12. If multiple sensors exist, should models be built separately for each sensor or jointly?
13. Which evaluation metrics are expected for anomaly detection?
14. Which forecasting metrics should be used, such as MAE, RMSE, or MAPE?
15. Are there domain-specific acceptable ranges for temperature, pH, dissolved oxygen, and pressure?
16. Is real-time anomaly detection required, or is offline analysis sufficient?

---

## 9. Initial Technical Plan

The initial development plan is:

1. Understand the dataset structure.
2. Inspect timestamps and sampling frequency.
3. Identify all available environmental variables.
4. Perform data-quality checks.
5. Conduct exploratory time-series analysis.
6. Define an appropriate anomaly detection strategy.
7. Develop and evaluate anomaly detection models.
8. Define forecasting targets and forecasting horizon.
9. Develop and evaluate forecasting models.
10. Compare results and select appropriate approaches.
11. Build visualizations and generate environmental insights.
12. Document the complete methodology and results.
