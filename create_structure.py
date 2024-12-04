import os

def create_project_structure(base_path="project_root"):
    structure = {
        "app": [
            "__init__.py",
            "main.py",
            "database.py",
            {"models": ["__init__.py", "cours.py", "session.py", "evaluation.py", "users.py"]},
            {"routes": ["__init__.py", "cours_routes.py", "session_routes.py", "evaluation_routes.py", "user_routes.py"]},
            {"services": ["__init__.py", "cours_service.py", "session_service.py", "evaluation_service.py", "user_service.py"]},
            {"utils": ["__init__.py", "validators.py", "common.py"]},
        ],
        "scripts": ["seed_data.py", "reset_db.py"],
        "tests": ["__init__.py", "test_cours.py", "test_sessions.py", "test_evaluations.py", "test_users.py"],
        ".": ["requirements.txt", ".env", "README.md"],
    }

    def create_files_and_dirs(base, items):
        for item in items:
            if isinstance(item, str):
                # Cria arquivo
                open(os.path.join(base, item), "w").close()
            elif isinstance(item, dict):
                # Cria subdiretório
                for folder, subitems in item.items():
                    folder_path = os.path.join(base, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    create_files_and_dirs(folder_path, subitems)

    os.makedirs(base_path, exist_ok=True)
    create_files_and_dirs(base_path, structure["app"])
    create_files_and_dirs(os.path.join(base_path, "scripts"), structure["scripts"])
    create_files_and_dirs(os.path.join(base_path, "tests"), structure["tests"])
    for file in structure["."]:
        open(os.path.join(base_path, file), "w").close()

    print(f"Estrutura criada em: {os.path.abspath(base_path)}")

# Execute o script
if __name__ == "__main__":
    create_project_structure()
