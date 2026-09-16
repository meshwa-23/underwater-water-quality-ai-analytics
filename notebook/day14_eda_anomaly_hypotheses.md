# Day 14 — EDA and Anomaly Hypotheses

## 1. Objective

The objective of Day 14 is to review the exploratory data analysis findings, identify possible temporal patterns, assess sensor-data quality, and document hypotheses for anomaly detection.

---

## 2. EDA and Anomaly Hypotheses

Based on the available water-quality variables, the following observations and hypotheses were considered:

| Area | Observation / Question | Anomaly Hypothesis |
|------|-------------------------|--------------------|
| pH | pH values show variation over time | Sudden changes in pH may indicate unusual water-quality behaviour |
| Solids | Solids values have substantial variation | Abrupt changes may indicate potential anomalies |
| Conductivity | Conductivity changes across observations | Sudden spikes or drops may indicate unusual conditions |
| Turbidity | Turbidity varies between observations | Extreme or sudden changes may indicate abnormal water conditions |
| Sensor stability | Some measurements show changing values over consecutive observations | Large short-term changes may require anomaly investigation |

These are hypotheses rather than confirmed anomalies and will require quantitative validation in later experiments.

---

## 3. Temporal Patterns

The dataset was converted into a timestamped time series.

Time-based features were created:

- Hour
- Day of week
- Day
- Month

Lag and rolling features were also created to represent historical behaviour:

- One-step lag features
- Three-observation rolling mean
- Three-observation rolling standard deviation

These features allow future experiments to examine whether recent historical behaviour can help identify unusual observations or predict future water-quality values.

---

## 4. Sensor Quality Assessment

The available dataset contains the following water-quality variables:

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic carbon
- Trihalomethanes
- Turbidity

The dataset does not currently contain temperature, dissolved oxygen, or pressure measurements.

Potential sensor/data-quality issues to monitor include:

- Missing values
- Extreme values
- Sudden changes between consecutive observations
- Irregular temporal behaviour
- Duplicate timestamps
- Measurement distributions that differ substantially between sensors

The engineered lag and rolling features intentionally use historical observations to reduce future-data leakage.

---

## 5. Peer Insight

**Peer Insight:**  
A useful peer observation was that anomaly detection should not depend only on extreme individual sensor values. The relationship between recent observations and multiple sensors should also be considered when identifying unusual behaviour.

---

## 6. Hypothesis

**Hypothesis:**  
Combining current water-quality measurements with recent historical features such as lag values, rolling mean, and rolling standard deviation may improve the identification of unusual water-quality behaviour compared with using raw sensor measurements alone.

This hypothesis will be evaluated quantitatively during subsequent modelling experiments.

---

## 7. Week-2 Package

The Week-2 project package contains:

- Dataset versioning and validation
- Timestamped train/validation/test datasets
- Feature-engineering notebook
- Engineered datasets
- Time-based features
- Lag features
- Rolling statistical features
- Cross-sensor features
- Feature-definition documentation
- EDA and anomaly hypotheses
- Sensor-quality observations
- Peer insight
- Hypothesis for future experimentation

---

## 8. Next Steps

The next phase will focus on establishing baseline anomaly-detection and forecasting experiments and evaluating the engineered features using appropriate metrics.git 