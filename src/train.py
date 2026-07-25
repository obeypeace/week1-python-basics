import logging
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def train_model():
    logger.info("loading data for training")
    df = pd.read_csv("data.csv")

    # drop rows with missing values
    df = df.dropna(subset=["Age"])
    X = df[["Age", "Fare", "Pclass"]]
    y = df["Survived"]

    logger.info(f"Training on {len(X)} rows")
    # instantiate the model
    model = LogisticRegression()
    model.fit(X, y)

    joblib.dump(model, "model.joblib")
    logger.info("model saved to model.joblib")


if __name__ == "__main__":
    train_model()
