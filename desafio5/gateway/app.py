import requests
from flask import Flask, jsonify

app = Flask(__name__)

USERS_URL = "http://users_service:3001"
ORDERS_URL = "http://orders_service:3002"

@app.route('/users')
def proxy_users():
    try:
        resp = requests.get(f"{USERS_URL}/users_data")
        return jsonify(resp.json())
    except:
        return jsonify(
                {
                    "error": "Users service indisponível"
                }
            ), 503

@app.route('/orders')
def proxy_orders():
    try:
        resp = requests.get(f"{ORDERS_URL}/orders_data")
        return jsonify(resp.json())
    except:
        return jsonify(
            {
                "error": "Orders service indisponível"
            }
        ), 503
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)