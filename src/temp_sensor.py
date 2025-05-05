# src/temp_sensor.py
import random

def read_temperature_c():
    """Return a simulated temperature (°C)."""
    return round(20 + random.random() * 10, 2)

def sample_temperatures(n=50):
    """Generate n samples and return list of floats."""
    return [read_temperature_c() for _ in range(n)]

