from flask import Flask, jsonify, make_response
from flask_migrate import Migrate

from models import db, FantasyShop

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.get("/fantasy_shops/<string:name>")
def get_fantasy_shops(name):
   fantasy_shop = FantasyShop.query.filter(FantasyShop.name == name).first()
   fantasy_shop = {
    "name":fantasy_shop.name,
    "category":fantasy_shop.category,
    "location": fantasy_shop.location,
    "description":fantasy_shop.description,
    "in_use":fantasy_shop.in_use
   }
   response = make_response(
    jsonify(fantasy_shop),
    200
   )
   return response



    