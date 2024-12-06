from flask_smorest import Blueprint

from .analyse_service import AnalyseService

analyse = Blueprint('analyse', 'analyse', url_prefix='/api/analyse', description='Analyse course data')

analyse_service = AnalyseService()

@analyse.route('/<cours_id>')
def analyse_per_course(cours_id: str):
    return analyse_service.compute_analyse_per_course(cours_id)