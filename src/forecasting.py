import joblib


def load_forecasting_model(model_path):
    artifact = joblib.load(model_path)
    return artifact


def prepare_forecasting_features(data, feature_columns):
    missing_columns = [
        column
        for column in feature_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing forecasting features: {missing_columns}"
        )

    return data[feature_columns].copy()


def predict_next_ph(model_artifact, data):
    model = model_artifact["model"]
    imputer = model_artifact["imputer"]
    features = model_artifact["features"]

    X = prepare_forecasting_features(
        data,
        features
    )

    X_imputed = imputer.transform(X)

    predictions = model.predict(X_imputed)

    results = data.copy()
    results["predicted_next_ph"] = predictions

    return results
