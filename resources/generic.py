from flask_restful import Resource
from http import HTTPStatus
from flask import request
from models.models import CatalogBaseModel


class GenericApi:
    """
    This is the generic Api
    """
    schema = None
    model: CatalogBaseModel = None


class RetrieveUpdateDeleteResource(Resource, GenericApi):
    """
    This base class implements the Retrieving items by id
    updating items by id
    deleting items by id (soft delete)
    """

    def get(self, id):
        """
        This method implements the get request for the specific record
        :param id: id of the element
        :return:
        """
        record = self.model.get_by_id(id)

        if record is None:
            return {'message': 'No records found'}, HTTPStatus.NOT_FOUND

        return record.data, HTTPStatus.OK

    def put(self, id):
        """
        This method will implement the PUT request
        :param id: id to be updated
        :return: Update Entity if found else NOT_FOUND status
        """
        record = self.model.get_by_id(id)

        if record is None:
            return {'message': 'No records found'}, HTTPStatus.NOT_FOUND

        data_json = request.get_json()
        errors = self.schema.validate(data=data_json)
        if errors:
            return {'message': 'Validation Error', 'error': errors}, HTTPStatus.BAD_REQUEST

        data = self.schema.load(data=data_json)
        for name, value in data.items():
            setattr(record, name, value)
        record.save()
        return record.data, HTTPStatus.OK

    def delete(self, id):
        """
        Delete implementation of Entity
        :param id: id of the Entity
        :return: NO_CONTENT if the Entity is deleted and NOT_FOUND
        if the entity is not found
        """
        record = self.model.get_by_id(id)

        if record is None:
            return {'message': 'No records found'}, HTTPStatus.NOT_FOUND

        record.is_deleted = True
        record.save()
        return {}, HTTPStatus.NO_CONTENT


class ListAPIResource(Resource, GenericApi):
    """
    This base implementation is for APIs where we get all the items and post to
    create new records
    """
    list_schema = None

    def get(self):
        """
        This is generic get implementation
        :return:
        """
        items = self.model.get_all_items()

        return self.list_schema.dump(items), HTTPStatus.OK

    def post(self):
        """
        This is generic Post implementation
        :return:
        """
        data_json = request.get_json()

        errors = self.schema.validate(data=data_json)
        if errors:
            return {'message': 'Validation Error', 'error': errors}, HTTPStatus.BAD_REQUEST
        data = self.schema.load(data=data_json)
        model_entity = self.model(**data)
        model_entity.save()
        return model_entity.data, HTTPStatus.CREATED
