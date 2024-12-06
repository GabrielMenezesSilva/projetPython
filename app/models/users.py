from pymongo import MongoClient
from app.models.config import get_db

def create_user(user, session_id):
	db = get_db()
	users_collection = db['users']
	sessions_collection = db['sessions']
	
	# Insere o usuário
	user_id = users_collection.insert_one(user).inserted_id
	
	# Liga o usuário à sessão
	sessions_collection.update_one(
		{ "_id": session_id },
		{ "$addToSet": { "users": user_id } }
	)
	print(f"Usuário {user['name']} inserido e ligado à sessão {session_id}!")

def is_admin(user_id):
	db = get_db()
	user = db['users'].find_one({ "_id": user_id })
	return user.get('role') == 'admin'