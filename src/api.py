from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import joblib
import pandas as pd
from src.logger_config import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)

app = FastAPI()


@app.get(
    "/"
)  # decorator that says - when some1 sends a get request to the /path, run the function right below this line
def read_root():
    logger.info("root endpoint called")
    return {"message": "Hello, this is my first API"}


# the function returns a dictionary, fastapi auto converts it to json
# the standard format APIs communicate in


class GreetingRequest(BaseModel):
    name: str


@app.post("/greet")
def greet(request: GreetingRequest):
    logging.info(f"greet endpoint called with name={request.name}")
    return {"message": f"hello, {request.name}!"}


class PassengerRequest(BaseModel):
    age: float
    fare: float
    pclass: int


class CaptainsSalute(BaseModel):
    name: str


@app.post("/salute")
def captains_salute(message: CaptainsSalute):
    logging.info(f"captains salute to passenger {message.name}")
    return {
        "message": f"Hello {message.name}, its your captain - Peace, welcome aboard!!"
    }


@app.post("/passenger-summary")
def passenger_summary(passenger: PassengerRequest):
    logger.info(
        f"Passenger summary requested: age={passenger.age}, fare={passenger.fare}, pclass={passenger.pclass}"
    )

    if passenger.pclass not in [1, 2, 3]:
        logger.warning(f"Invalid pclass received: {passenger.pclass}")
        raise HTTPException(status_code=400, detail="pclass must be 1, 2, or 3")

    return {
        "age": passenger.age,
        "fare": passenger.fare,
        "pclass": passenger.pclass,
        "note": f"Passenger in class {passenger.pclass} paid {passenger.fare} fare",
    }


model = joblib.load("model.joblib")
logger.info("model loaded successfully")


@app.post("/predict")
def predict(passenger: PassengerRequest):
    logger.info(
        f"Prediction requested: age={passenger.age}, fare={passenger.fare}, pclass={passenger.pclass}"
    )

    if passenger.pclass not in [1, 2, 3]:
        logger.warning(f"Invalid pclass received: {passenger.pclass}")
        raise HTTPException(status_code=400, detail="pclass must be 1, 2, or 3")

    if passenger.age < 0 or passenger.age > 120:
        logger.warning(f"Invalid age received: {passenger.age}")
        raise HTTPException(status_code=400, detail="age must be between 0 and 120")

    if passenger.fare < 0:
        logger.warning(f"Invalid fare received: {passenger.fare}")
        raise HTTPException(status_code=400, detail="fare must be non-negative")

    features = pd.DataFrame(
        [[passenger.age, passenger.fare, passenger.pclass]],
        columns=["Age", "Fare", "Pclass"],
    )
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "survived_prediction": int(prediction),
        "survival_probability": round(float(probability), 3),
    }


# predict_proba returns probabilities for each possible class, per row.
# Since Survived has two possible outcomes (0 = didn't survive, 1 = survived),
# for one passenger you get back something like: [[0.234, 0.766]]
