# Dataset Schema and Structure Note

## 1. Purpose

This document defines the expected structure, fields, labels, targets and metadata required for the underwater water-quality AI/ML project.

The final dataset must be inspected and validated against this expected structure before model development.

---

## 2. Expected Dataset Type

The dataset is expected to contain time-stamped underwater environmental measurements.

Primary data type:

- Multivariate time-series data
- Numerical environmental measurements
- Timestamped observations
- Potentially multiple sensors, locations or monitoring periods

---

## 3. Expected Files

The final dataset may contain one or more of the following:

| File | Expected Purpose |
|---|---|
| Main measurement file | Timestamped water-quality observations |
| Metadata file | Sensor/location/unit information |
| Label file | Existing anomaly or event labels, if available |
| Documentation | Dataset description, measurement definitions and collection details |

Actual files must be confirmed after dataset inspection.

---

## 4. Expected Core Columns

| Column | Type | Role | Expected Meaning |
|---|---|---|---|
| timestamp | datetime | Primary temporal feature | Date and time of measurement |
| temperature | numerical | Input feature / possible target | Water temperature |
| pH | numerical | Input feature / possible target | Acidity/alkalinity |
| dissolved_oxygen | numerical | Input feature / possible target | Dissolved oxygen concentration |
| pressure | numerical | Input feature / possible target | Underwater pressure |
| other_variables | numerical/categorical | Input features | Additional available environmental measurements |

The exact column names, units and data types must be confirmed from the actual dataset.

---

## 5. Important Metadata

The following metadata should be identified where available:

- Sensor ID
- Monitoring location
- Latitude/longitude or location identifier
- Depth
- Timestamp and timezone
- Sampling frequency
- Measurement units
- Sensor type/model
- Calibration information
- Data collection period
- Environmental or weather context
- Data source
- Quality-control indicators
- Missing-value indicators

---

## 6. Anomaly Target

### If anomaly labels exist

Expected label information may include:

- Anomaly flag
- Normal/anomaly class
- Anomaly type
- Event ID
- Annotation timestamp
- Annotation source

Possible representation:

```text
0 = Normal
1 = Anomaly