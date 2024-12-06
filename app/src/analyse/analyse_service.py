from ..cours.cours import Cours
from .analyse_reposiotry import AnalyseRepository

class AnalyseService:
    def __init__(self):
        self.repository = AnalyseRepository()
    
    def compute_analyse_per_course(self, cours_id: str) -> dict:
        get_evaluations: list = self.repository.get_all_evaluations_by_course(cours_id)
        get_evaluations[0].pop('_id')
        print(get_evaluations)
        # TODO: do the analyse
        # for example: Compute the average of the evaluations
        return get_evaluations# {"date": {}, "prof": {}}