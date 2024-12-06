from flask import Flask, request, jsonify
from flask_cors import CORS
from models.evaluation import insert_evaluation
from models.users import create_user
from models.session import get_session

# Crée une instance de l'application Flask
app = Flask(__name__)
# Active CORS pour l'application Flask
CORS(app)

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
    app.run(host='0.0.0.0', port=3000)