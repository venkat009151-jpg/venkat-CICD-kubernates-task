from flask import Flask, render_template
import requests

app = Flask(__name__)

BACKEND_URL = "http://host.docker.internal:8081/api/info"

@app.route("/")
def home():
    try:
        response = requests.get(BACKEND_URL)
        data = response.json()
    except Exception:
        data = {
            "application": "Unavailable",
            "version": "-",
            "service": "Backend not reachable",
            "status": "Down"
        }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)