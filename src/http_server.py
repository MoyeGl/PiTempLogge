# src/http_server.py
from flask import Flask, jsonify
import glob, os

LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs"))
app = Flask(__name__)

def get_latest_reading():
    logs = sorted(glob.glob(os.path.join(LOG_DIR, "*.log")))
    if not logs:
        return {}
    last = logs[-1]
    with open(last) as f:
        line = f.readlines()[-1]
    timestamp, temp = line.strip().split(", ")
    return {"timestamp": timestamp, "temperature_c": float(temp)}

@app.route("/latest")
def latest():
    return jsonify(get_latest_reading())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
