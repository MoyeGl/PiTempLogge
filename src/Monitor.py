# src/monitor.py
import matplotlib.pyplot as plt
from temp_sensor import sample_temperatures

def plot_samples(n=50):
    temps = sample_temperatures(n)
    plt.figure()
    plt.plot(temps, marker="o")
    plt.title(f"{n} Simulated Temperature Readings")
    plt.xlabel("Sample #")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_samples()
