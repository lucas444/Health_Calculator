from flask import Flask, jsonify, request
from utils import add_numbers, subtract_numbers

app = Flask(__name__)

@app.route('/')
def home():
    return "Benvenue"

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    result = add_numbers(data['a'], data['b'])
    return jsonify({"result": result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    result = subtract_numbers(data['a'], data['b'])
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

