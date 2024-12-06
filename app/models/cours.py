from app.models.cours import create_course
from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['sms_nomades']
    return db

def create_course(course):
    db = get_db()
    collection = db['courses']
    collection.insert_one(course)
    print(f"Curso {course['name']} inserido!")

def seed_database():
    courses = [
        { "id": "WD", "name": "Web Designer (WD)" },
        { "id": "WPR", "name": "Web Programmer (WPR)" },
        { "id": "MWAD", "name": "Mobile Web Application Developer (MWAD)" },
        { "id": "PSE", "name": "Python Software Engineer (PSE)" },
        { "id": "PDA", "name": "Data Analysis (PDA)" },
        { "id": "DAF", "name": "Data Science pour la Finance (DAF)" },
        { "id": "DMM", "name": "Digital Marketing (DMM)" }
    ]

    print("Inserindo cursos...")
    for course in courses:
        create_course(course)
        print(f"Curso {course['name']} inserido!")

if __name__ == "__main__":
    seed_database()
