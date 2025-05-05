import os
from src import logger

def test_log_file_created():
    test_temp = 25.5
    logger.log_reading(test_temp)

    files = os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs")))
    assert any(f.endswith(".log") for f in files)
