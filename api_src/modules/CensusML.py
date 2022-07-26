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
    #
    # async def run_inference(self, payload) -> dict:
    #
    #     payload = pd.DataFrame(payload.dict(by_alias=True), index=[0])
    #
    #     X, _, _, _ = process_data(X=payload,
    #                               categorical_features=self.cat_features,
    #                               label=None,
    #                               training=False,
    #                               encoder=self.encoder,
    #                               lb=self.lb)
    #     preds = inference(self.model, X)
    #     label = self.lb.inverse_transform(preds)[0]
    #     output = {"pred_result": {"salary": label}}
    #     return output
