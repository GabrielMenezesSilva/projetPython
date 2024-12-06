from pymongo import MongoClient

def get_db():
	client = MongoClient('mongodb://localhost:27017/')
	db = client['sms_nomades']
	return db

def insert_evaluation(data):
    db = get_db()
    collection = db['evaluations']
    collection.insert_one(data)
    print("Données enregistrées dans MongoDB")