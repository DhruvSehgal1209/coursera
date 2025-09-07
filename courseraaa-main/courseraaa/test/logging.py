from api.logging_setup import setup_logging
import os

def test_log_file_created():
    logger = setup_logging()
    logger.info("Test log")
    assert os.path.exists('api_logs.log')
