import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_info():
    try:
        response = requests.get('http://service_a:5001/users')
        users = response.json()

        output = "<h1>Consumindo Serviço A</h1>"
        for user in users:
            output += f"<p>Usuário {user['name']} ativo desde {user['since']}</p>"
        return output
    except Exception as ex:
        return f"Erro ao contatar serviço A: {str(ex)}"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)