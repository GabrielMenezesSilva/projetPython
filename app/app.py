from flask import Flask, request, jsonify
from flask_smorest import Api
from flask_cors import CORS

from src.cours.cours_controller import cours
from src.analyse.analyse_controller import analyse
from config.mango_db import insert_evaluation


class APIConfig:
    API_TITLE = "SMS Nomades"
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/docs'
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Crée une instance de l'application Flask
app = Flask(__name__)
app.config.from_object(APIConfig)

# Active CORS pour l'application Flask
CORS(app)

api = Api(app)

api.register_blueprint(cours)
api.register_blueprint(analyse)

# Définir une route pour l'endpoint /api/submit avec la méthode POST
@app.route('/api/submit', methods=['POST'])
def submit():
    # Vérifie si la méthode de la requête est POST
    if request.method == 'POST':
        try:
            # Récupère les données JSON de la requête
            data = request.get_json()
            print("Requête POST reçue")
            
            # Vérifie si les données sont nulles
            if data is None:
                print("Aucune donnée reçue")
                return jsonify({"message": "Aucune donnée reçue"}), 400
            
            # Insère l'évaluation dans la base de données
            insert_evaluation(data)
            
            # Retourne une réponse JSON avec un message de succès
            return jsonify({"message": "Données reçues avec succès !"}), 200
        except Exception as e:
            # En cas d'erreur, affiche l'erreur et retourne une réponse JSON avec un message d'erreur
            print(f"Erreur : {e}")
            return jsonify({"message": "Erreur lors du traitement des données."}), 500

if __name__ == '__main__':
    # Démarre l'application Flask sur l'hôte 0.0.0.0 et le port 3000
    app.run(debug=True, host='0.0.0.0', port=3000)