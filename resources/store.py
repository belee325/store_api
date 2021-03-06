from flask_restful import Resource, reqparse
from resources.user_register import UserRegister
from models.store_model import StoreModel



class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message' : 'store not found'} , 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'a store with name {} already exists'.format(name)}, 400
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message':'An error has occurred'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if not store:
            return {'message': 'store does not exist'}, 400
        store.delete_from_db()
        return {'message': 'store deleted'}, 200


class StoreList(Resource):
    def get(self):
        return {'stores' : [store.json() for store in StoreModel.query.all()]}