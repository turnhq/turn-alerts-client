from marshmallow import Schema, fields


class ResponseDataSchema(Schema):
    loc = fields.List(fields.String)
    msg = fields.String()
    type = fields.String()


class InvalidResponseSchema(Schema):
    detail = fields.List(fields.Nested(ResponseDataSchema()))
