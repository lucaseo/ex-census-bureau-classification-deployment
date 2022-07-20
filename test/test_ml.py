import pytest

import numpy as np
import pandas as pd
from joblib import load
from sklearn.model_selection import train_test_split

from ml_src.ml.data import process_data
from ml_src.ml.model import compute_model_metrics, inference


@pytest.fixture
def data():
    return pd.read_csv("./data/prepared/census_cleaned.csv", encoding='utf-8', sep='\t')

@pytest.fixture
def model():
    return load("./model/model.joblib")

@pytest.fixture
def encoder():
    return load("./model/encoder.joblib")

@pytest.fixture
def lb():
    return load("./model/lb.joblib")

def test_lb_class(lb):
    assert len(lb.classes_) == 2

def test_null_sample_train(data):
    assert data.shape == data.dropna().shape, "Dropping null changes shape."

def test_preprocess_output_train(data, encoder, lb):
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
    X, y, _, _ = process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb,
    )

    assert data.shape[0] == np.shape(X)[0], "samples changed after processing (X)"
    assert data.shape[0] == np.shape(y)[0], "samples changed after processing (y)"
    assert data.shape[1] <= np.shape(X)[1], "issue in categorical feature encoding"
    assert np.ndim(y) == 1, "issue with label"

def test_model_performance(data, model, encoder, lb):
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

    train, test = train_test_split(data, test_size=0.20, random_state=42)

    X, y, _, _ = process_data(
        test,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb,
    )

    preds = inference(model, X)
    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert fbeta >= 0.5, "baseline model performance below expectation"



