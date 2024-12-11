from marshmallow import Schema, fields

class AnalyseResponse(Schema):
    x = fields.List(fields.Str)
    y = fields.List(fields.Float)
    type_chart = fields.Str()