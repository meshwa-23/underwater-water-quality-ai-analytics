# Experiment Plan

## 1. Objective

Design a reproducible experimental workflow for detecting anomalies and forecasting future underwater water-quality parameters.

The workflow should allow different methods to be compared using the same dataset preparation, splits and evaluation criteria.

---

## 2. Reproducible Workflow

Raw Dataset
↓
Data Validation
↓
Data Cleaning
↓
Exploratory Data Analysis
↓
Temporal Sorting
↓
Train / Validation / Test Split
↓
Feature Engineering
↓
Baseline Models
↓
Advanced Models
↓
Evaluation
↓
Model Comparison
↓
Final Results and Visualization

---

## 3. Anomaly Detection Experiments

### Baseline Method

Statistical methods:

- Rolling Z-score
- IQR or MAD-based detection

Purpose:

Provide a simple reference against which machine-learning methods can be compared.

### Advanced Method

Isolation Forest

Purpose:

Detect unusual observations without requiring anomaly labels.

### Optional Method

Local Outlier Factor (LOF)

This will only be used if the dataset characteristics justify it.

### Evaluation

If anomaly labels exist:

- Precision
- Recall
- F1-score
- Confusion matrix
- PR-AUC where appropriate

If anomaly labels do not exist:

- Number of detected anomalies
- Anomaly detection rate
- Distribution of anomaly scores
- Temporal consistency
- Visual inspection of detected events
- Domain/mentor validation where possible

---

## 4. Forecasting Experiments

### Baseline Methods

1. Persistence / last-value prediction
2. Moving average
3. Linear Regression

### Advanced Methods

1. Random Forest Regression
2. XGBoost Regression

### Conditional Sequence Model

LSTM/GRU may be considered only if:

- Dataset size is sufficient
- Temporal patterns justify it
- Baseline and tree-based models have been evaluated first

---

## 5. Forecasting Evaluation

Primary metrics:

- MAE
- RMSE

Additional metric:

- R²

MAPE may be used only when the target values make percentage error meaningful and the denominator is not close to zero.

---

## 6. Processing Performance

For each major experiment record:

- Training time
- Prediction time
- Total processing time
- Dataset size
- Hardware/software environment

Processing time will be reported as a secondary comparison metric.

---

## 7. Project-Specific Experiment

The main project-specific experiment will combine:

- Historical environmental measurements
- Temporal features
- Lag features
- Rolling statistics
- Multivariate relationships

The objective is to determine whether combining historical temporal information with multiple water-quality variables improves anomaly detection and forecasting performance compared with simple baselines.

---

## 8. Fair Comparison Rules

All models should use:

- The same cleaned dataset
- The same temporal train/validation/test split
- The same target definition
- The same forecast horizon
- No future information in features
- Training-only preprocessing where applicable

---

## 9. Experiment Selection

The final model will be selected based on:

1. Predictive performance
2. Generalization to unseen future data
3. Robustness
4. Processing time
5. Interpretability
6. Suitability for the available dataset