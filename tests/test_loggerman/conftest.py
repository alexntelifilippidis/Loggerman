import pytest
from src.loggerman.logger import LoggermanLogger

@pytest.fixture
def logger():
    # Ensure fresh singleton instance for each test
    logger_instance = LoggermanLogger(name="TestLoggerman", level="DEBUG", propagate=True)
    yield logger_instance