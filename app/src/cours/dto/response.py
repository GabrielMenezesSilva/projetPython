from marshmallow import Schema, fields

class CourseResponse(Schema):
    id = fields.Str()
    name = fields.Str()