from pymongo import MongoClient
from datetime import datetime
from app.models.config import get_db

def create_session(session):
	db = get_db()
	collection = db['sessions']
	collection.insert_one(session)
	print(f"Sessão {session['name']} inserida!")

def get_session(session_id):
	db = get_db()
	session = db['sessions'].find_one({ "_id": session_id })
	return session

if __name__ == "__main__":
	course_id = "WPR"  # Substitua pelo ID real do curso
	year = 2024
	month = 8
	users = []  # Lista de IDs de usuários

	# Recupera o nome do curso
	db = get_db()
	course = db['courses'].find_one({ "id": course_id })
	if not course:
		print(f"Curso com ID {course_id} não encontrado!")
	else:
		# Gera o session_id no formato especificado
		session_id = f"{course_id}_{year}_{month:02d}"
		
		# Gera o nome da sessão
		session_name = f"{course['name']} - {month}/{year}"
		
		# Cria o documento da sessão
		session = {
			"_id": session_id,
			"name": session_name,
			"course_id": course_id,
			"users": users,
			"month": month,
			"year": year,
			"created_at": datetime.now()
		}
		
		# Insere a sessão no banco de dados
		create_session(session)