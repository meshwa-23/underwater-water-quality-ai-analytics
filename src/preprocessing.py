import pandas as pd

SENSOR_COLUMNS = [
    "ph",
    "Hardness",
    "Solids",
    "Chloramines",
    "Sulfate",
    "Conductivity",
    "Organic_carbon",
    "Trihalomethanes",
    "Turbidity"
]

FORECAST_FEATURES = [
    "ph",
    "Hardness",
    "Solids",
    "Chloramines",
    "Sulfate",
    "Conductivity",
    "Organic_carbon",
    "Trihalomethanes",
    "Turbidity",
    "hour",
    "day_of_week",
    "day",
    "month",
    "ph_lag_1",
    "ph_rolling_mean_3",
    "ph_rolling_std_3"
]

def load_data(file_path):
    return pd.read_csv(file_path)

def prepare_timestamp(df):
    df = df.copy()

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df = df.sort_values("timestamp").reset_index(drop=True)

    return df

def create_temporal_features(df):
    df = prepare_timestamp(df)

    if "timestamp" not in df.columns:
        raise ValueError("Dataset must contain a timestamp column.")

    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek
    df["day"] = df["timestamp"].dt.day
    df["month"] = df["timestamp"].dt.month

    df["ph_lag_1"] = df["ph"].shift(1)
    df["ph_rolling_mean_3"] = df["ph"].rolling(3).mean()
    df["ph_rolling_std_3"] = df["ph"].rolling(3).std()

    return df

def create_forecasting_target(df):
    df = df.copy()
    df["ph_next"] = df["ph"].shift(-1)
    return df

def prepare_forecasting_data(df):
    df = create_temporal_features(df)
    df = create_forecasting_target(df)

    required_columns = FORECAST_FEATURES + ["ph_next"]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    return df.dropna(
        subset=required_columns
    ).reset_index(drop=True)

def prepare_anomaly_data(df):
    missing_columns = [
        column for column in SENSOR_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing sensor columns: {missing_columns}"
        )

    return df[SENSOR_COLUMNS].copy()
