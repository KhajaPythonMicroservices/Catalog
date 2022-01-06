from marshmallow import (
    fields, validate
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
