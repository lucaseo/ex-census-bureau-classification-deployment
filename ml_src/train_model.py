# Script to train machine learning model.

# Add the necessary imports for the starter code.
import json

import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import dump

from ml.data import process_data
from ml.model import train_model, compute_model_metrics, inference



def compute_model_metrics_with_slice(model, data, encoder, lb, cat_features, sliced_feature: str, label: str):

    result: dict = {}

    for cls in data[sliced_feature].unique():
        data_slice = data[data[sliced_feature]==cls].copy()

        X, y, _, _ = process_data(
            data_slice,
            categorical_features=cat_features,
            label=label,
            training=False,
            encoder=encoder,
            lb=lb
        )

        preds = inference(model, X)
        precision, recall, fbeta = compute_model_metrics(y, preds)

        result[cls] = {
            "precision": precision,
            "recall": recall,
            "fbeta": fbeta,
            "sample_count": len(y)
        }

    return {"sliced_feature": result}





# Add code to load in the data.
if __name__ == "__main__":
    data = pd.read_csv("./../data/prepared/census_cleaned.csv", sep='\t', encoding='utf-8')

    # Optional enhancement, use K-fold cross validation instead of a train-test split.
    train, test = train_test_split(data, test_size=0.20)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )

    # Proces the test data with the process_data function.
    X_test, y_test, _, _ = process_data(
        test, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
    )

    model = train_model(X_train, y_train)

    # Train and save a model.
    dump(model, "./../model/model.joblib")
    dump(encoder, "./../model/encoder.joblib")
    dump(lb, "./../model/lb.joblib")

    # function that outputs the performance of the model on slices of the data.
    # Suggestion: for simplicity, the function can just output the performance on slices of just the categorical features.

    preds = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)

    slice_col_name = "workclass"
    metrics_sliced = compute_model_metrics_with_slice(model, test, encoder, lb, cat_features, slice_col_name, "salary")

    with open("./../resources/model_output/slice-output-{}.json".format(slice_col_name), "w") as fp:
        json.dump(metrics_sliced, fp)
