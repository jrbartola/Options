from flask import Flask, jsonify, request
from options import get_vertical_spreads

app = Flask(__name__)

@app.route('/')
def index():
    contract_type = request.args.get('contractType')
    symbol = request.args.get('symbol')
    return jsonify(get_vertical_spreads(symbol, contract_type))

if __name__ == '__main__':
    app.run(debug=True)