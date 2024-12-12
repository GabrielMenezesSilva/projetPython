from pymongo import MongoClient

class AnalyseRepository:
    def __init__(self, db_url='mongodb://localhost:27017/', db_name='sms_nomades'):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]

    def get_data(self, collection_name, query):
        collection = self.db[collection_name]
        return list(collection.find(query))

    def close(self):
        self.client.close()
        
    def get_all_evaluations_by_course(self, cours_id: str):
        return self.get_data("evaluations", {"Formationsuivie.id": cours_id})
    
    def get_all_evaluations_by_professor(self, professor_id: str):
        return list(self.db.evaluations.find({"professor_id": professor_id, "rating_prof": {"$exists": True}}))