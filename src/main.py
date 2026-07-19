import logging
from src.data import load_data, summarize_data

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Starting data pipeline")
    df = load_data("data.csv")
    logger.info(f"Loaded data with shape {df.shape}")
    summarize_data(df)
    logger.info("finished summarizing data")


if __name__ == "__main__":
    main()
