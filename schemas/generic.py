from marshmallow import (
    Schema, fields, validate, ValidationError
)


class BaseCatalogSchema(Schema):
    """
    This is the base catalog schema
    """
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
