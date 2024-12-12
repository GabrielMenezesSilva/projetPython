from flask import Flask, request, jsonify
from flask_smorest import Api
from flask_cors import CORS

from src.cours.cours_controller import cours
from src.analyse.analyse_controller import analyse_controller
from config.mango_db import insert_evaluation


class APIConfig:
    API_TITLE = "SMS Nomades"
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/docs'
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Cria uma instância do aplicativo Flask
app = Flask(__name__)
app.config.from_object(APIConfig)

# Ativa CORS para a aplicação Flask
CORS(app)

api = Api(app)

# Registra os blueprints
api.register_blueprint(cours)
api.register_blueprint(analyse_controller)

# Rota de teste
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Server is running!"}), 200

# Rota de submissão
@app.route('/api/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        print(f"Requisição POST recebida com dados: {data}")

        if not data:
            return jsonify({"message": "Aucune donnée reçue"}), 400

        insert_evaluation(data)
        return jsonify({"message": "Données reçues avec succès !"}), 200
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"message": "Erro ao processar dados."}), 500

if __name__ == '__main__':
    # Inicia o servidor Flask
    print("Servidor iniciado na porta 3000")
    app.run(debug=True, host='0.0.0.0', port=3000)