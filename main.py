from fastapi import FastAPI
from pydantic import BaseModel
from utils import create_model
import pandas as pd

class Input(BaseModel):
    gender: str
    job: str
    city: str
    state: str
    zip: int
    lat: float
    long: float
    city_pop: int
    category: str
    merchant: str
    merch_lat: float
    merch_long: float
    amt: float
    age: int
    trans_year: int
    trans_month: int
    trans_day: int
    trans_hour: int
    trans_minute: int
    trans_second: int
    trans_number: int
    card_type: str
    card_industry: str
    state_fraud_ratio_2019:float
    state_fraud_ratio_2020:float
    merchant_fraud_ratio_2019:float
    merchant_fraud_ratio_2020:float
    job_fraud_ratio_2019: float
    job_fraud_ratio_2020: float
    category_fraud_ratio_2019: float
    category_fraud_ratio_2020: float

app = FastAPI()

model = create_model(loss="binary_crossentropy")
model.load_weights("training/model_weights.h5")

@app.post('/')
async def home(req: Input):
    result = model.predict(pd.DataFrame(req))[0][0] > 0.23
    return {'resultado': result}