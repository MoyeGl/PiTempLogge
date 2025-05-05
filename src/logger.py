# src/logger.py
import os
from datetime import datetime, timedelta
import glob

LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs"))
os.makedirs(LOG_DIR, exist_ok=True)

def log_reading(temp_c: float):
    timestamp = datetime.utcnow().isoformat()
    filename = os.path.join(LOG_DIR, datetime.utcnow().strftime("%Y-%m-%d") + ".log")
    with open(filename, "a") as f:
        f.write(f"{timestamp}, {temp_c}\n")

def rotate_logs(retention_days: int = 7):
    cutoff = datetime.utcnow() - timedelta(days=retention_days)
    for path in glob.glob(os.path.join(LOG_DIR, "*.log")):
        date_str = os.path.basename(path).replace(".log", "")
        file_date = datetime.strptime(date_str, "%Y-%m-%d")
        if file_date < cutoff:
            os.remove(path)
