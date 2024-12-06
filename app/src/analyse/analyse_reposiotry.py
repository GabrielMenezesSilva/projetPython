import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.mango_db import get_db
from ..cours.cours import Cours

class AnalyseRepository:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['evaluations']
    
    def get_all_evaluations_by_course(self, cours_id: str):
        return [evaluation for evaluation in self.collection.find({'Formationsuivie.id': cours_id})]