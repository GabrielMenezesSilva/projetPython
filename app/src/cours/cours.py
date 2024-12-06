class Cours:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name
        }

    @staticmethod
    def from_dict(data: dict[str, str]) -> 'Cours':
        return Cours(id=data.get("id"), name=data.get("name"))
    
    def __str__(self) -> str:
        return f"Cours<{self.id} - {self.name}>"
    def __repr__(self) -> str:
        return self.__str__()