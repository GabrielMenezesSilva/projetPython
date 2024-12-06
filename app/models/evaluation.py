from app.models.config import get_db

def insert_evaluation(data):
	db = get_db()
	collection = db['evaluations']
	collection.insert_one(data)
	print("Données enregistrées dans MongoDB")