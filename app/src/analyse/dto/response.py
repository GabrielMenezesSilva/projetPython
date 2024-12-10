class AnalyseDTO:
    # Initialisation de la classe AnalyseDTO avec les attributs id, name, created_at et updated_at
    def __init__(self, id, name, created_at, updated_at):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

    # Méthode pour convertir les attributs de l'objet en dictionnaire
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
