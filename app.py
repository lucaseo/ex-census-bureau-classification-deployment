# uvicorn main:app --host 0.0.0.0 --port 80 --reload

import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api_src.services.inference import CensusClassificationInferenceService
from api_src.modules.DataClass import InputData

if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")

app = FastAPI(title="census_inference_api",
              version="v0.1",
              description="Inference API for census dataset")

census_clf = CensusClassificationInferenceService()


@app.on_event("startup")
async def startup_load_artifact():
    census_clf.load_artifact()

@app.get("/")
async def say_hello_world():
    return JSONResponse(
        content={
            "msg": "Welcome to Census ML Inference API"
        }
    )

@app.post("/prediction")
async def predict(payload: InputData):

    output = census_clf.run_inference(payload=payload)
    return await output


if __name__ == "__main__":
    uvicorn.run(app="app:app",
                host="127.0.0.1",
                port=8000,
                reload=True)
