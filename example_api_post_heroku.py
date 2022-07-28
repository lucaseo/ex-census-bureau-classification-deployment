import json
import requests

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

if __name__ == "__main__":

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