import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_data(filepath: str) -> pd.DataFrame:
    """Reads a CSV file and returns it as a DataFrame."""
    logger.info(f"Loading data from {filepath}")
    return pd.read_csv(filepath)


def get_summary_stats(df: pd.DataFrame) -> dict:
    """Compute summary info for a DataFrame, returning it as a dict instead of printing."""
    return {
        "shape": df.shape,
        "dtypes": df.dtypes,
        "describe": df.describe() if not df.empty else None,
    }

def summarize_data(df: pd.DataFrame) -> None:
    """Print basic summary statistics for a DataFrame."""
    if df.empty:
        logger.warning("Received an empty DataFrame — nothing to summarize.")
        return
    logger.debug("Summarizing dataframe")
    stats = get_summary_stats(df)
    print(f"Shape: {stats['shape']}")
    print("\nColumn types:")
    print(stats['dtypes'])
    print("\nSummary stats:")
    print(stats['describe'])
