class Analyse:
    # Initialisation de la classe AnalyseDTO avec les attributs id, name, created_at et updated_at
    def __init__(self, name, date, x, y, chart_type = "line"):
        self.name = name
        self.date = date
        self.x = x
        self.y = y
        self.chart_type = chart_type
        
    # Méthode pour convertir les attributs de l'objet en dictionnaire
    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "x": self.x,
            "y": self.y,
            "chart_type": self.chart_type   
        }
    
