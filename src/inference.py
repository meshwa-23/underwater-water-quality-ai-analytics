import os

from src.preprocessing import (
    load_data,
    prepare_timestamp,
    create_temporal_features,
)

from src.anomaly_detection import (
    load_anomaly_model,
    detect_anomalies,
)

from src.forecasting import (
    load_forecasting_model,
    predict_next_ph,
)


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

ANOMALY_MODEL_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "day22_final",
    "final_isolation_forest.joblib",
)

FORECAST_MODEL_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "day22_final",
    "final_random_forest.joblib",
)


def run_inference(input_path, output_path):

    print("Loading input data...")
    data = load_data(input_path)

    print("Preparing timestamps...")
    data = prepare_timestamp(data)

    print("Creating temporal features...")
    data = create_temporal_features(data)

    print("Loading final anomaly model...")
    anomaly_model = load_anomaly_model(
        ANOMALY_MODEL_PATH
    )

    print("Running anomaly detection...")
    results = detect_anomalies(
        anomaly_model,
        data
    )

    print("Loading final forecasting model...")
    forecasting_model = load_forecasting_model(
        FORECAST_MODEL_PATH
    )

    print("Running pH forecasting...")
    results = predict_next_ph(
        forecasting_model,
        results
    )

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    results.to_csv(
        output_path,
        index=False
    )

    print("Results saved to:")
    print(output_path)

    return results


if __name__ == "__main__":

    input_file = os.path.join(
        BASE_DIR,
        "data",
        "processed",
        "test_v1_engineered.csv"
    )

    output_file = os.path.join(
        BASE_DIR,
        "experiments",
        "day26_inference_output.csv"
    )

    run_inference(
        input_file,
        output_file
    )