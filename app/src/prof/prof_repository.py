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
        
