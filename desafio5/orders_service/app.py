from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders_data')
def get_orders():
    return jsonify(
        {
            "orders": [
                "Pedido #001",
                "Pedido #002"
            ]
        }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002)