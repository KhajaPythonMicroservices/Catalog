from flask_restful import Resource
from models.models import CatalogBrand
from http import HTTPStatus
from flask import request
from schemas.catalogbrand import CatalogBrandSchema

catalog_brand_schema = CatalogBrandSchema()
catalog_brand_list_schema = CatalogBrandSchema(many=True)


class CatalogBrandListResource(Resource):
    """
    This resource will be used to get, post the Catalog Brand
    """
    def get(self):
        """
        This method will return the catalog brands
        :return: Brands of the catalog
        """
        catalog_brands = CatalogBrand.get_all_items()

        return catalog_brand_list_schema.dump(catalog_brands), HTTPStatus.OK

    def post(self):
        """
        This method will add the catalog brand
        :return:
        """
        catalog_brand_json = request.get_json()

        errors = catalog_brand_schema.validate(data=catalog_brand_json)
        if errors:
            return {'message': 'Validataion Error', 'error': errors}, HTTPStatus.BAD_REQUEST
        data = catalog_brand_schema.load(data=catalog_brand_json)
        catalog_brand = CatalogBrand(**data)
        catalog_brand.save()
        return catalog_brand.data, HTTPStatus.CREATED



