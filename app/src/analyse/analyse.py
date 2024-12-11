class Analyse:
    # Initialisation de la classe AnalyseDTO avec les attributs id, name, created_at et updated_at
    def __init__(self, name, created_at, x, y):
        self.name = name
        self.created_at = created_at
        self.x = x
        self.y = y
        self.type_chart = 'line'
        
    # Méthode pour convertir les attributs de l'objet en dictionnaire
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at            
        }
    
