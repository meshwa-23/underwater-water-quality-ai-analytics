# Revised Research Framing

## 1. Refined Research Question

How can time-stamped underwater water-quality measurements be used to detect anomalous environmental conditions and forecast future water-quality parameters using machine learning?

## 2. Sub-Questions

1. What constitutes an anomalous observation or period in the underwater water-quality time series?
2. Which environmental parameters contribute most to detecting anomalies?
3. How well can historical measurements predict future values of temperature, pH, dissolved oxygen, pressure, and other available parameters?
4. Which anomaly detection method performs best compared with a statistical baseline?
5. Which forecasting model provides the best predictive performance while remaining interpretable?

## 3. Inputs

The system will use available time-stamped underwater measurements, including:

- Timestamp
- Temperature
- pH
- Dissolved Oxygen (DO)
- Pressure
- Other available water-quality variables

## 4. Measurable Outputs

### Anomaly Detection

The system will produce:

- Binary anomaly flag: 0 = normal, 1 = anomaly
- Anomaly score
- Timestamp of detected anomaly
- Affected parameter(s)
- Number and percentage of anomalous observations

### Forecasting

The system will produce:

- Predicted future values of selected environmental parameters
- Forecast horizon based on the available sampling frequency
- MAE
- RMSE
- R²
- MAPE where appropriate

## 5. Candidate Methods

### Anomaly Detection

Baseline:

- Rolling Z-score
- IQR / MAD-based detection

Machine Learning:

- Isolation Forest

Optional:

- Local Outlier Factor (LOF)

### Forecasting

Baselines:

- Persistence / last-value prediction
- Moving average
- Linear Regression

Machine Learning:

- Random Forest Regression
- XGBoost Regression

Sequence models:

- LSTM / GRU only if the dataset size and temporal structure justify their use.

## 6. Scope

### Included

- Historical time-series analysis
- Data quality assessment
- Anomaly detection
- Future-value forecasting
- Model comparison
- Visualization and interpretation

### Not Included

- Hardware development
- Sensor manufacturing
- On-device deployment
- Real-time hardware integration
- Autonomous control of underwater systems

## 7. Current Success Criteria

The project will be considered successful if:

1. The dataset is correctly understood and cleaned.
2. A reproducible anomaly detection pipeline is developed.
3. Anomaly detection methods can be compared using measurable criteria.
4. Forecasting models can predict future environmental parameters with acceptable error.
5. Models are evaluated using appropriate time-series validation.
6. Results are interpretable and supported by experimental evidence.
