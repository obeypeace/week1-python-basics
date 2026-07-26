from src.data import load_data, summarize_data
from src.logger_config import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)


def main() -> None:
    logger.info("Starting data pipeline")
    df = load_data("data.csv")
    logger.info(f"Loaded data with shape {df.shape}")
    summarize_data(df)
    logger.info("finished summarizing data")


if __name__ == "__main__":
    main()
