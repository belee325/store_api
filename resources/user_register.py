from flask_restful import Resource, reqparse
from models.user_model import UserModel

class UserRegister(Resource):
    user_parser = reqparse.RequestParser()
    reqparse.Argument
    user_parser.add_argument('username',type = str, required = True)
    user_parser.add_argument('password', type=str, required=True)
    def post(self):
        data = UserRegister.user_parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message':'the username already exists!'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message':'user has been created successfully'}, 201