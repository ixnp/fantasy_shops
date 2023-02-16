from flask import Flask, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from db import db
from models import FantasyShop, InventoryItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.json.compact = False


migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

class FantasyShops(Resource):
   def get(self):
      fantasy_shop_list = [fs.to_dict() for fs in FantasyShop.query.all()]

      response = make_response(
         fantasy_shop_list,
         200
      )
      return response
api.add_resource(FantasyShops, '/fantasy_shops')

class InventoryItems(Resource):
   def get(self):
      inventory_items_list = [fs.to_dict() for fs in InventoryItem.query.all()]

      response = make_response(
         inventory_items_list,
         200
      )
      return response
api.add_resource(InventoryItems, '/inventory_items')


    