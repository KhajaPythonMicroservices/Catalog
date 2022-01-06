from marshmallow import (
    Schema, fields, validate, ValidationError
)

class CatalogBrandSchema(Schema):
    """
    This represents the catalog brand schema
    """
    class Meta:
        ordered = True

    id = fields.Integer(dump_only=True)
    brand = fields.String(required=True, validate=[validate.Length(max=256)])
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
