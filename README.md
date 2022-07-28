# Census Classification ML API

Income category prediction based on Census data (Udacity Nanodegree project)

## Key takaways from this project

- Data EDA (`jupyter notebook`)
- ML model training (`scikit-learn`)
  - feature engineering
  - model training
  - ML model performance monitoring on sliced data
- Unit test (with `pytest`)
- Version Control
  - code (`git`, `Github`)
  - data (`git`, `DVC`)
  - model (`git`, `DVC`)
- Remote storage (`AWS S3`)
- Continuous Integration (`Github Actions`)
- API development (`FastAPI`)
- Continuous Deployment (`Heroku`)


## Sending reqest to API

Via Python script (refer to `example_api_post_heroku.py`)

```python
import json
import requests

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

url = "https://census-classification-udacity.herokuapp.com/prediction"

data = {"age": 40,
        "workclass": "Private",
        "education": "Doctorate",
        "marital-status": "Married-civ-spouse",
        "occupation": "Prof-specialty",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "native-country": "United-States",
        "hours-per-week": 60}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.status_code)
print(response.json())
```