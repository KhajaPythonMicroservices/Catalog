from extensions import db


class CatalogBaseModel:
    """
    This class represents the base Model
    """
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    is_deleted = db.Column(db.Boolean(), default=False, server_default="False", nullable=False)

    def save(self) -> None:
        """
        This method will be used to save the data to the database
        """
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        """
        This method will be used to soft delete the record
        """
        self.is_deleted = True
        self.save()

    def restore(self) -> None:
        """
        This method is used to restore the soft deleted record
        """
        self.is_deleted = False
        self.save()

    @classmethod
    def get_all_items(cls):
        """
        This method will get all the items
        """
        return cls.query.filter(cls.is_deleted.is_(False)).all()


class CatalogType(CatalogBaseModel, db.Model):
    """
    This class represents type of the catalog
    """

    type = db.Column(db.String, nullable=False)


class CatalogBrand(CatalogBaseModel, db.Model):
    """
    This class represents brand of the Catalog
    """
    brand = db.Column(db.String, nullable=False)
    items = db.relationship('CatalogItem', backref='catalog_brand', lazy=True)

    @property
    def data(self):
        return {
            'id': self.id,
            'brand': self.brand
        }


class CatalogItem(CatalogBaseModel, db.Model):
    """
    This model represents the catalog item
    """
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, default=0.0)
    catalog_type_id = db.Column(
        db.Integer(),
        db.ForeignKey("catalog_type.id"),
        nullable=False)
    brand_id = db.Column(
        db.Integer,
        db.ForeignKey('catalog_brand.id'),
        nullable=False)
    available_stock = db.Column(db.Integer, default=0)
    max_stock = db.Column(db.Integer, default=0)
    restock_threshold = db.Column(db.Integer, default=0)



