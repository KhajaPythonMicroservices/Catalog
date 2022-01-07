from models.models import CatalogItem
from schemas.catalogschema import CatalogItemSchema
from resources.generic import ListAPIResource, RetrieveUpdateDeleteResource


class CatalogItemListResource(ListAPIResource):
    """
    This resource will be used to get, post the Catalog Item
    """
    model = CatalogItem
    schema = CatalogItemSchema()
    list_schema = CatalogItemSchema(many=True)


class CatalogItemResource(RetrieveUpdateDeleteResource):
    """
    This resource will be used to update/delete the Catalog Item
    """
    model = CatalogItem
    schema = CatalogItemSchema()
