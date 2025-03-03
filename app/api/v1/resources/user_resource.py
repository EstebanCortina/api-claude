from flask import request, jsonify
from flask_restful import Resource, Api
from marshmallow import ValidationError

from app.schemas import UserSchema
from app.services import UserService
from app.utils.http_status import HttpStatus

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserListResource(Resource):
    def get(self):
        users = UserService.get_all_users()
        return users_schema.dump(users), HttpStatus.OK
    
    def post(self):
        try:
            user_data = user_schema.load(request.get_json())
            user = UserService.create_user(user_data)
            return user_schema.dump(user), HttpStatus.CREATED
        except ValidationError as err:
            return {'message': 'Validation error', 'errors': err.messages}, HttpStatus.BAD_REQUEST

class UserResource(Resource):
    def get(self, user_id):
        user = UserService.get_user_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, HttpStatus.NOT_FOUND
        
        return user_schema.dump(user), HttpStatus.OK
    
    def put(self, user_id):
        try:
            user_data = user_schema.load(request.get_json(), partial=True)
            user = UserService.update_user(user_id, user_data)
            
            if not user:
                return {'message': 'User not found'}, HttpStatus.NOT_FOUND
                
            return user_schema.dump(user), HttpStatus.OK
        except ValidationError as err:
            return {'message': 'Validation error', 'errors': err.messages}, HttpStatus.BAD_REQUEST
    
    def delete(self, user_id):
        result = UserService.delete_user(user_id)
        if not result:
            return {'message': 'User not found'}, HttpStatus.NOT_FOUND
            
        return '', HttpStatus.NO_CONTENT

def register_user_resources(bp):
    api = Api(bp)
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<int:user_id>')