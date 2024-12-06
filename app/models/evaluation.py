# Importa a função get_db do módulo app
from app import get_db

# Função para inserir uma avaliação no banco de dados
def insert_evaluation(data):
	# Obtém a conexão com o banco de dados
	db = get_db()
	# Seleciona a coleção 'evaluations' no banco de dados
	collection = db['evaluations']
	# Insere o documento 'data' na coleção 'evaluations'
	collection.insert_one(data)
	# Imprime uma mensagem de confirmação
	print("Données enregistrées dans MongoDB")