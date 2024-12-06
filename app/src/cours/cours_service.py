from .cours_repository import CoursRepository
from .cours import Cours

class CoursService:
    def __init__(self):
        self.repository = CoursRepository()
    
    def get_all_courses(self) -> list[Cours]:
        return self.repository.get_all_courses()