from pydantic import BaseModel, Field




class InputData(BaseModel):
    age: int
    workclass: str
    education: str
    marital_status: str = Field(alias="marital-status")
    occupation: str
    relationship: str
    race: str
    sex: str
    native_country: str = Field(alias="native-country")
    hours_per_week: int = Field(alias="hours-per-week")