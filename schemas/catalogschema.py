from builtins import filter

from attr import validate
from marshmallow import (
    fields, validate, validates, ValidationError
)

from schemas.generic import BaseCatalogSchema


class CatalogBrandSchema(BaseCatalogSchema):
    """
    This represents the Catalog Brand Schema
    """
    brand = fields.String(required=True, validate=[validate.Length(max=256)])


class CatalogTypeSchema(BaseCatalogSchema):
    """
    This represents the CatalogType Schema
    """
    type = fields.String(required=True, validate=[validate.Length(max=256)])


class CatalogItemSchema(BaseCatalogSchema):
    """
    This represents the Catalog Item
    """
    name = fields.String(required=True, validate=[validate.Length(max=256)])
    description = fields.String(validate=[validate.Length(max=1000)])
    price = fields.Float()
    catalog_type_id = fields.Integer()
    brand_id = fields.Integer()
    # todo: Add validation that available_stock cannot be less than 0
    available_stock = fields.Integer()
    # todo: Add validation that max_stock cannot be less than 0
    max_stock = fields.Integer()
    # todo: Add validation that restock_threshold cannot be less than 0
    restock_threshold = fields.Integer()


    @validates('price')
    def validate_price(self, value):
        if value < 0:
            return ValidationError('Price must be greater than 0')


