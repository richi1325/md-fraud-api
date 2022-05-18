from fastapi import FastAPI, Body
from pydantic import BaseModel
from utils import create_model
import pandas as pd
import json

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

with open("./codificaciones.json","r") as f:
    data = json.load(f)

@app.post('/')
async def home(req: Input = Body(...)): 
    req = req.dict()
    req["gender"] = data["gender"].index(req["gender"])
    req["job"] = data["job"].index(req["job"])
    req["city"] = data["city"].index(req["city"])
    req["state"] = data["state"].index(req["state"])
    req["category"] = data["category"].index(req["category"])
    req["merchant"] = data["merchant"].index(req["merchant"])
    req["card_type"] = data["card_type"].index(req["card_type"])
    req["card_industry"] = data["card_industry"].index(req["card_industry"])
    result = float(model.predict(pd.DataFrame([req]))[0][0])
    result = result > 0.23
    return {'is_fraud': result}
