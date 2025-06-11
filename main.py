import os
import json

from flask import Flask, send_file, request, jsonify

app = Flask(__name__)

steps = 0
target_steps = 8000

@app.route("/")
def index():
    return send_file('src/index.html')

target_steps_done = 0
@app.route("/steps", methods=['POST'])
def update_steps():
    global steps
    data = request.get_json()
    if data and 'steps' in data:
        steps = int(data['steps'])
        if steps >= target_steps:
            global target_steps_done
            target_steps_done += 1
        steps = steps - (target_steps_done*target_steps)
        return jsonify({"status": "success", "current_steps": steps, "target_steps": target_steps})
    return jsonify({"status": "error", "message": "Invalid request body"}), 400

@app.route("/data", methods=['GET'])
def get_data():
    return jsonify({"steps": steps, "target_steps": target_steps})

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
