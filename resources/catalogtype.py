from models.models import CatalogType

from resources.generic import ListAPIResource, RetrieveUpdateDeleteResource
from schemas.catalogschema import CatalogTypeSchema


class CatalogTypeListResource(ListAPIResource):
    """
    This is catalog type list resource
    """
    model = CatalogType
    schema = CatalogTypeSchema()
    list_schema = CatalogTypeSchema(many=True)


class CatalogTypeResource(RetrieveUpdateDeleteResource):
    """
    This is for CatalogTypeResource
    """
    model = CatalogType
    schema = CatalogTypeSchema()
