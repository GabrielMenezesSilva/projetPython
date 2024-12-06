import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.mango_db import get_db
from .cours import Cours

class CoursRepository:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['cours']
    
    def get_all_courses(self) -> list[Cours]:
        return [Cours.from_dict(cours) for cours in self.collection.find()]