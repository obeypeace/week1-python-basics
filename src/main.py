import pandas as pd

def summarize_data(filepath: str) -> None:
    """Load a CSV and print basic summary statistics."""
    df = pd.read_csv(filepath)
    print(f"Shape: {df.shape}")
    print("\nColumn types:")
    print(df.dtypes)
    print("\nSummary stats:")
    print(df.describe())

if __name__ == "__main__":
    summarize_data("data.csv")