# Literature Review and Method Comparison

## 1. Purpose of the Literature Review

The purpose of this literature review is to understand existing approaches used for:

- Water-quality monitoring
- Underwater/environmental monitoring
- Time-series anomaly detection
- Water-quality forecasting
- IoT-based environmental data analytics
- Machine learning-based prediction

The review is used to identify suitable baseline and advanced methods for the proposed underwater water-quality AI analytics system.

The main variables of interest are timestamped environmental measurements such as temperature, pH, dissolved oxygen, pressure, and other available water-quality parameters.

---

# 2. Core Domain Concepts

## 2.1 Artificial Intelligence and Machine Learning

Machine learning enables a system to learn patterns from historical environmental measurements and use those patterns for anomaly detection and prediction.

For this project, supervised and unsupervised learning may both be relevant.

- Supervised learning can be used for forecasting when historical target values are available.
- Unsupervised or semi-supervised methods can be used for anomaly detection when labelled anomalies are unavailable.

---

## 2.2 Time-Series Data

Water-quality measurements are time-series data because every observation is associated with a timestamp.

Therefore, the order of observations is important.

Important characteristics include:

- Temporal trends
- Seasonality
- Short-term fluctuations
- Long-term changes
- Lag relationships
- Correlations between environmental variables

Randomly shuffling observations during model evaluation could cause temporal data leakage.

Therefore, chronological train-validation-test splitting should be preferred.

---

## 2.3 Water-Quality Monitoring

Important water-quality indicators include:

- Temperature
- pH
- Dissolved oxygen
- Pressure
- Salinity
- Turbidity
- Conductivity
- Other available environmental measurements

These variables can interact with each other and may exhibit nonlinear relationships.

Recent reviews indicate that IoT and ML systems are increasingly being used for continuous water-quality monitoring, anomaly detection, prediction, and early-warning applications.

---

## 2.4 IoT Data Analytics

IoT-based monitoring systems can continuously collect environmental measurements through sensors.

A typical architecture is:

Sensors
→ Data Transmission
→ Data Storage
→ Data Processing
→ Machine Learning
→ Monitoring / Prediction

Although the current project is software-only, understanding IoT data characteristics is important because the dataset represents the type of timestamped measurements that environmental sensors can generate.

---

## 2.5 Anomaly Detection

Anomaly detection identifies observations that significantly differ from expected behavior.

Examples include:

- Sudden pH changes
- Unexpected dissolved oxygen drops
- Temperature spikes
- Pressure abnormalities
- Sensor failures
- Unusual combinations of multiple parameters

When labelled anomalies are unavailable, unsupervised methods are useful.

---

## 2.6 Forecasting

Forecasting predicts future environmental parameter values from historical observations.

Possible targets include:

- Future temperature
- Future pH
- Future dissolved oxygen
- Future pressure

Forecasting performance should be evaluated using metrics such as:

- MAE
- RMSE
- MAPE where appropriate
- R² for regression-style evaluation

---

# 3. Related Literature and Systems

## Study 1 — Water Quality Estimation and Anomaly Detection Review

This review examines water-quality estimation and anomaly detection approaches in water-management systems.

The study highlights the importance of online sensors, wireless networks, and AI-based anomaly detection.

### Relevance

This provides a foundation for the anomaly-detection component of the proposed project.

### Limitation

The review covers a broad water-management domain rather than focusing specifically on underwater time-series forecasting.

---

## Study 2 — Smart Water Management Using IoT, AI and ML

A 2026 review examines the integration of IoT, AI and machine learning for water-quality monitoring.

The review identifies applications including high-frequency monitoring, predictive forecasting, anomaly detection and early-warning systems.

Machine-learning approaches discussed include random forests, gradient boosting and deep neural networks.

### Relevance

The study strongly supports the overall architecture of combining environmental measurements with ML-based prediction and anomaly detection.

### Limitation

It is a broad review and does not provide a single model suitable for every water-quality dataset.

---

## Study 3 — Hybrid Decision Tree Models for Short-Term Water-Quality Prediction

This study evaluates hybrid models based on Random Forest and XGBoost for short-term prediction of multiple water-quality indicators.

The dataset contained 1,875 hourly observations from a river system.

The variables included:

- Water temperature
- Dissolved oxygen
- pH
- Specific conductance
- Turbidity
- Fluorescent dissolved organic matter

The study reported strong prediction performance from CEEMDAN-RF and CEEMDAN-XGBoost.

### Relevance

This is highly relevant because the variables overlap with the proposed project's temperature, DO and pH forecasting objectives.

### Limitation

The study uses a specific river dataset and additional signal-processing techniques that may not be necessary for our dataset.

---

## Study 4 — Tree-Based Models for Dissolved Oxygen Prediction

A study compared Random Forest, conditional Random Forest, Ranger and XGBoost for predicting dissolved oxygen using water-quality and hydrological variables.

XGBoost achieved the strongest reported performance in the evaluated feature-selection settings, with R² values around 0.84–0.85.

### Relevance

This supports Random Forest and XGBoost as strong candidate forecasting models for environmental variables.

### Limitation

The study uses additional remote-sensing and hydrological features that may not exist in our dataset.

---

## Study 5 — IoT-Driven Ensemble Prediction of Dissolved Oxygen

An IoT-based aquaculture study used temperature, pH and dissolved oxygen measurements collected at 15-minute intervals.

Random Forest, Gradient Boosting and XGBoost were compared and combined into an ensemble.

The ensemble achieved R² values around 0.84–0.86 for dissolved oxygen and around 0.91 for WQI in that study.

### Relevance

The sampling structure and variables are closely related to the proposed environmental monitoring problem.

### Limitation

The data were collected from a specific aquaculture environment over a relatively short period, limiting direct generalization.

---

## Study 6 — Short-Term Dissolved Oxygen Forecasting

A recent study compared Random Forest, LSTM and Transformer approaches for daily dissolved oxygen forecasting at three stream sites.

Water temperature was identified as an important predictor across the evaluated locations.

### Relevance

This provides evidence for comparing tree-based methods with sequence models when sufficient temporal data are available.

### Limitation

LSTM/Transformer models require more data, computational resources and careful temporal validation.

---

## Study 7 — IoT-Based Pond Water-Quality Monitoring

An IoT monitoring system used sensors for:

- Temperature
- pH
- Dissolved oxygen
- Salinity
- Turbidity

The system transmitted measurements to a cloud platform and included machine-learning-based anomaly prediction.

### Relevance

The system architecture is similar to the type of data pipeline represented by the proposed project.

### Limitation

The system is focused on aquaculture pond monitoring rather than general underwater environmental conditions.

---

## Study 8 — Intelligent Water-Quality Monitoring with Machine Learning

A 2026 system combined IoT sensing, cloud integration and on-device machine learning.

The system measured pH, TDS, temperature and turbidity and used a neural network to classify water impurity events.

### Relevance

It demonstrates how environmental sensor data can be combined with ML for automated abnormal-condition detection.

### Limitation

The system focuses on categorical impurity-event classification rather than continuous time-series anomaly scoring and forecasting.

---

# 4. Literature Comparison Table

| Study / System | Data | Approach | Metrics / Results | Limitation | Relevance |
|---|---|---|---|---|---|
| Water Quality Estimation & Anomaly Detection Review | Water-management sensor data and existing studies | ML anomaly detection review | Comparative review | Broad domain | High for anomaly detection |
| Smart Water Management Review | IoT water-quality data and existing studies | RF, Gradient Boosting, DNN and IoT analytics | Review of reported performance | Broad review | High for overall architecture |
| Hybrid Decision Tree Water Prediction | 1,875 hourly observations | CEEMDAN-RF, CEEMDAN-XGBoost | Average MAPE 3.90% and 3.71% for the two hybrid approaches | Specific river dataset | Very high for forecasting |
| Tree-Based DO Prediction | Water-quality + hydrological data | RF, cRF, Ranger, XGBoost | XGBoost R² ≈ 0.84–0.85 | Additional features required | High |
| IoT DO/WQI Prediction | Temperature, pH, DO at 15-min intervals | RF, GB, XGBoost, ensemble | DO R² ≈ 0.84–0.86; WQI ≈ 0.91 | Short/specific aquaculture dataset | Very high |
| DO Forecasting | Daily stream measurements | RF, LSTM, Transformer | Comparative forecasting study | Sequence models require sufficient data | High |
| IoT Pond Monitoring | Temperature, pH, DO, salinity, turbidity | IoT + ML anomaly prediction | System-level monitoring | Aquaculture-specific | High |
| Intelligent Water Monitoring | pH, TDS, temperature, turbidity | Neural network + TinyML | 99.28% event classification accuracy | Classification rather than forecasting | Medium |