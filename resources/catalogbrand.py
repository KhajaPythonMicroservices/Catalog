from models.models import CatalogBrand
from schemas.catalogschema import CatalogBrandSchema
from resources.generic import ListAPIResource, RetrieveUpdateDeleteResource


class CatalogBrandListResource(ListAPIResource):
    """
    This resource will be used to get, post the Catalog Brand
    """
    model = CatalogBrand
    schema = CatalogBrandSchema()
    list_schema = CatalogBrandSchema(many=True)


class CatalogBrandResource(RetrieveUpdateDeleteResource):
    model = CatalogBrand
    schema = CatalogBrandSchema()
