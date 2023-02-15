from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class FantasyShop(db.Model):
    __tablename__ = 'fantasy_shop'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    location = db.Column(db.String)
    description = db.Column(db.String)
    in_use = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<FantasyShop Name:{self.name}, category:{self.category}, location:{self.location}, description:{self.description}, in_use:{self.in_use}>'