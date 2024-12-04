from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Configurar a conexão com o MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['sms_nomades']
collection = db['evaluations']

print(collection)

@app.route('/api/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            # Recebe os dados do corpo da requisição
            data = request.get_json()
            print("Requête POST reçue")  # Debug: confirmar que a requisição POST foi recebida
            
            # Verifica se os dados foram recebidos corretamente
            if data is None:
                print("Aucune donnée reçue")  # Debug: nenhuma dado recebido
                return jsonify({"message": "Aucune donnée reçue"}), 400  # Retorna uma resposta de erro 400 (Bad Request)
            
            # Aqui, você pode processar os dados, por exemplo, analisar ou salvar no banco de dados
            print(f"Données reçues : {data}")  # Exemplo de debug - imprime os dados recebidos no terminal
            
            # Salva os dados no MongoDB
            collection.insert_one(data)
            print("Données enregistrées dans MongoDB")  # Debug: confirma que os dados foram salvos no MongoDB
            
            # Envia uma resposta de sucesso
            return jsonify({"message": "Données reçues avec succès !"}), 200  # Retorna uma resposta de sucesso 200 (OK)
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