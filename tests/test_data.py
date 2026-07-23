import pandas as pd
import pytest
from src.data import load_data, summarize_data, get_summary_stats

@pytest.fixture
def sample_df():
    """A small reusable DataFrame for tests that don't need real Titanic data."""
    return pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

def test_summarize_data_runs_without_error(sample_df):
    """A basic 'smoke test' — just confirms the function runs without crashing."""
    # df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    summarize_data(sample_df)

def test_load_data_returns_dataframe():
    """Checks that load_data returns the correct type and expected shape."""
    df = load_data("data.csv")
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 891  # Titanic dataset has 891 rows
    assert "Survived" in df.columns

def test_summarize_data_handles_missing_values():
    """Confirms summarize_data doesn't crash when data has missing values (NaN)."""
    df = pd.DataFrame({
        "a": [1, 2, None],
        "b": [4, None, 6]
    })
    summarize_data(df)  # should not raise an error

def test_summarize_data_handles_empty_dataframe(caplog):
    """Confirms summarize_data doesn't crash on an empty DataFrame."""
    df = pd.DataFrame()
    summarize_data(df)
    assert "empty" in caplog.text.lower()

def test_get_summary_stats_returns_correct_shape(sample_df):
    stats = get_summary_stats(sample_df)
    assert stats["shape"] == (3,2)