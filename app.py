from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            # Reçoit les données du corps de la requête
            data = request.get_json()
            print("Requête POST reçue")  # Debug: confirmer que la requête POST est reçue

            # Vérifie si les données sont reçues correctement
            if data is None:
                print("Aucune donnée reçue")  # Debug: aucune donnée reçue
                return jsonify({"message": "Aucune donnée reçue"}), 400

            # Ici, vous pouvez traiter les données, par exemple, analyser ou enregistrer dans la base de données
            print(f"Données reçues : {data}")  # Exemple de debug - imprimer les données reçues dans le terminal

            # Envoie une réponse de succès
            return jsonify({"message": "Données reçues avec succès !"}), 200
        except Exception as e:
            # S'il y a une erreur, renvoie une erreur 500
            print(f"Erreur : {e}")
            return jsonify({"message": "Erreur lors du traitement des données."}), 500
    else:
        print("Requête GET reçue")  # Debug: confirmer que la requête GET est reçue
        return jsonify({"message": "GET received"}), 200

if __name__ == '__main__':
    # Démarre le serveur Flask sur le port 3000 (ou tout autre port de votre choix)
    app.run(host='0.0.0.0', port=3000)
