import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_data(filepath: str) -> pd.DataFrame:
    """Reads a CSV file and returns it as a DataFrame."""
    logger.info(f"Loading data from {filepath}")
    return pd.read_csv(filepath)


def summarize_data(df: pd.DataFrame) -> None:
    """Load a CSV and print basic summary statistics."""
    logger.debug("Summarizing dataframe")
    print(f"Shape: {df.shape}")
    print("\nColumn types:")
    print(df.dtypes)
    print("\nSummary stats:")
    print(df.describe())
