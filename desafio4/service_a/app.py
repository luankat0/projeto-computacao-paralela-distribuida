from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def get_users():
    return jsonify(
        [
            {
                "id": 1, 
                "name": "Alice", 
                "since": "2023"
            },
            {
                "id": 2, 
                "name": "Bob", 
                "since": "2024"
            },
        ]
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)