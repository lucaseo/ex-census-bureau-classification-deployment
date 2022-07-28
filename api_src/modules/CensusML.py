import pandas as pd
from joblib import load
from ml_src.ml.data import process_data
from ml_src.ml.model import inference


class CensusSalaryClassificationModel:

    def __init__(self):
        self.model = None
        self.encoder = None
        self.lb = None

        self.cat_features = [
            "workclass",
            "education",
            "marital-status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "native-country",
        ]

    def load_artifact(self):
        self.model = load("./model/model.joblib")
        self.encoder = load("./model/encoder.joblib")
        self.lb = load("./model/lb.joblib")

