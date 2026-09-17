import numpy as np
import joblib


def load_anomaly_model(model_path):
    artifact = joblib.load(model_path)
    return artifact


def prepare_features(data, feature_columns):
    X = data[feature_columns].copy()
    return X


def detect_anomalies(model_artifact, data):
    model = model_artifact["model"]
    imputer = model_artifact["imputer"]
    features = model_artifact["features"]

    X = data[features].copy()
    X_imputed = imputer.transform(X)

    predictions = model.predict(X_imputed)
    scores = model.decision_function(X_imputed)

    results = data.copy()

    results["anomaly_flag"] = np.where(
        predictions == -1,
        1,
        0
    )

    results["anomaly_score"] = scores

    return results
