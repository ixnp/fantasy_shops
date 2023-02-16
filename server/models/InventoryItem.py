from db import db
from sqlalchemy_serializer import SerializerMixin

class InventoryItem(db.Model, SerializerMixin):
    __tablename__ = 'inventory_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    description = db.Column(db.String)
    cost = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    fantasy_shop_id = db.Column(db.Integer, db.ForeignKey('fantasy_shop.id'))

    serialize_rules = ('-fantasy_shop.inventory_items',)
   
    def __repr__(self):
        return f'<Inventory Item Name:{self.name}, category:{self.category}, description:{self.description}, cost:{self.cost}>'
