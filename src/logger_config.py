import logging

def setup_logging():
    """configure logging once for the entire application"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

def get_logger(name: str) -> logging.Logger:
    """getting a logger instance for a given module name"""
    return logging.getLogger(name)