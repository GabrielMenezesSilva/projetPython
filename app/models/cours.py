from app.models.cours import create_course



# TODO : Créer une fonction pour insérer les cours dans la base de données
# JE DEJA AJOUTé LES FORMATIONS DANS LA BASE DE DONNéES A LA MAIN MAIS JE VEUX FAIRE UNE FONCTION QUI FAIT LE MEME TRAVAIL ICI

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
