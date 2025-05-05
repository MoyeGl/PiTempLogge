# src/main.py
import time
from temp_sensor import read_temperature_c
from logger import log_reading, rotate_logs

def run_loop(interval_s: int = 10):
    while True:
        temp = read_temperature_c()
        log_reading(temp)
        rotate_logs(7)
        print(f"Logged {temp}°C")
        time.sleep(interval_s)

if __name__ == "__main__":
    run_loop()
