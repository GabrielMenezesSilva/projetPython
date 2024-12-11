import os
import sys
import json
import random
from datetime import datetime, timedelta
import pandas as pd
from pymongo import MongoClient

# Chemin du projet
project_path = os.path.abspath(os.path.join(os.getcwd(), '..', '..', '..'))
if project_path not in sys.path:
    sys.path.append(project_path)
    
from config.mango_db import get_db

# Fonction pour se connecter à la base de données
# def get_db():
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client['sms_nomades']
#     return db

# Classe pour l'analyse des données
class AnalyseRepository:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['evaluations']

    # Fonction pour insérer des données simulées dans la collection 'evaluations'
    def insert_sample_data(self, num_entries=100):
        """insérer des données simulées dans la collection 'evaluations'."""
        formations = ['JavaScript', 'Python', 'Data Science', 'Web Development']
        professors = ['Antonio Pisanello', 'Nico Fazio', 'Pierre-Marie Vial']
        for _ in range(num_entries):
            self.collection.insert_one({
                'Formationsuivie': random.choice(formations),
                'professor': random.choice(professors),
                'rating': random.randint(1, 5),  # Nota entre 1 e 5
                'Datesdelaformation': (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()
            })
        print(f"{num_entries} entrées simulées insérées avec succès.")

    def get_all_evaluations(self):
        return [evaluation for evaluation in self.collection.find()]
    
    def analyze_data(self):
        all_evaluations = self.get_all_evaluations()
        return all_evaluations
