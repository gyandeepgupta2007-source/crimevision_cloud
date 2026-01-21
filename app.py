from flask import Flask, request, jsonify

app = Flask(__name__)

latest_detection = {}

@app.route("/update", methods=["POST"])
def update_detection():
    global latest_detection
    latest_detection = request.json
    return jsonify({"status": "received"})

@app.route("/result", methods=["GET"])
def get_result():
    return jsonify(latest_detection)

@app.route("/")
def home():
    return "CrimeVision Cloud Server is Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
