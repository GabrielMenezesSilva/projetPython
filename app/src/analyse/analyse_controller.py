from flask_smorest import Blueprint
from flask import request, jsonify

from .analyse_service import AnalyseService

analyse_controller = Blueprint('analyse_controller', __name__)

@analyse_controller.route('/api/analyse/<cours_id>', methods=['GET'])
def analyse(cours_id):
	# Instanciar o serviço de análise
	analyse_service = AnalyseService()
	
	# Obter o ID do curso a partir dos parâmetros da requisição
	# cours_id = request.args.get(cours_id)
	
	# Chamar o método do serviço
	result = analyse_service.compute_analyse_per_course(cours_id)
	
	# Retornar o resultado como JSON
	return jsonify(result)

@analyse_controller.route('/api/courses/analyse', methods=['GET'])
def analyse():
	# Instanciar o serviço de análise
	analyse_service = AnalyseService()
	
	# Obter o ID do curso a partir dos parâmetros da requisição
	# cours_id = request.args.get(cours_id)
	
	# Chamar o método do serviço
	result = analyse_service.analyse_all_courses_per_time()
	
	# Retornar o resultado como JSON
	return jsonify(result)