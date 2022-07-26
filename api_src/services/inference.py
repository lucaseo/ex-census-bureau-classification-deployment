
# from api_src.settings import settings
import pandas as pd

from api_src.modules.CensusML import CensusSalaryClassificationModel
from ml_src.ml.data import process_data
from ml_src.ml.model import inference

class CensusClassificationInferenceService(CensusSalaryClassificationModel):

    def __init__(self):
        super().__init__()

    async def run_inference(self, payload) -> dict:

        payload = pd.DataFrame(payload.dict(by_alias=True), index=[0])

        X, _, _, _ = process_data(X=payload,
                                  categorical_features=self.cat_features,
                                  label=None,
                                  training=False,
                                  encoder=self.encoder,
                                  lb=self.lb)
        preds = inference(self.model, X)
        label = self.lb.inverse_transform(preds)[0]
        output = {"pred_result": {"salary": label}}
        return output

