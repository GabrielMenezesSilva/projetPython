from marshmallow import Schema, fields

class CourseResponse(Schema):
    id = fields.Str()
    name = fields.Str()
    # Champ pour l'identifiant du cours
    id = fields.Str()
    # Champ pour le nom du cours
    name = fields.Str()