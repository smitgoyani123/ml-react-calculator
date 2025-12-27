from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    v1 = float(data["value1"])
    v2 = float(data["value2"])
    op = data["operation"]

    if op == "add":
        result = v1 + v2
    elif op == "sub":
        result = v1 - v2
    elif op == "multiply":
        result = v1 * v2
    else:
        result = None

    return jsonify({"result": result})

app.run(port=5000)
