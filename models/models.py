from extensions import db


class CatalogBaseModel:
    """
    This class represents the base Model
    """
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    is_deleted = db.Column(db.Boolean(), default=False, server_default="False", nullable=False)


class CatalogType(CatalogBaseModel, db.Model):
    """
    This class represents type of the catalog
    """

    type = db.Column(db.String, nullable=False)
