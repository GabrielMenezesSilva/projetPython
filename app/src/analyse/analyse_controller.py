from flask_smorest import Blueprint
from .analyse_service import AnalyseService
from .dto.response import AnalyseResponse

# Define o blueprint para a API de análise de curso
analyse = Blueprint('analyse', 'analyse', url_prefix='/api/analyse/PSE', description='Analyse course data')

# Cria uma instância do serviço de análise
analyse_service = AnalyseService()

# Rota que recebe o `cours_id` como parâmetro na URL
@analyse.route('/<cours_id>')
@analyse.response(200, AnalyseResponse)  # Especifica o tipo de resposta esperado
def analyse_per_course(cours_id: str):
    """
    Rota que processa a análise de avaliações para um curso específico.
    :param cours_id: O identificador único do curso para análise
    :return: Dados da análise, formatados de acordo com o DTO `AnalyseResponse`
    """
    return analyse_service.compute_analyse_per_course(cours_id)