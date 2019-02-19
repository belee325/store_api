from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from resources.item import Item, ItemList
from resources.user_register import UserRegister
from resources.store import Store, StoreList
from security import *


app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)
jwt = JWT(app, authenticate, identify)  # /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')




if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(debug=True)
