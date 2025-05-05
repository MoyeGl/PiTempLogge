# PiTempLogger 🔥

Simulated temperature logger that mimics embedded system behavior using Python. Logs fake temperature readings, visualizes them, serves them via a REST API, and includes CI/CD with GitHub Actions.

## Features
- 📈 Random temperature generation
- 🗂 Daily log rotation
- 🌐 Flask HTTP server
- 🔁 CI/CD pipeline using GitHub Actions
- 🧪 Unit tests with coverage

## Run it
```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run main logger loop
python src/main.py

# Plot samples
python src/monitor.py

# HTTP server
python src/http_server.py
