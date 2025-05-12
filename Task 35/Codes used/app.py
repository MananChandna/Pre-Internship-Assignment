from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("fraud_model.pkl")

class InputData(BaseModel):
    data: dict

@app.post("/predict")
async def predict(input_data: InputData):
    try:
        input_values = list(input_data.data.values())
        prediction = model.predict([input_values])
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
