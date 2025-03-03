from werkzeug.security import generate_password_hash
from app import db
from app.models import User

class UserService:
    @staticmethod
    def create_user(user_data):
        user = User(
            username=user_data['username'],
            email=user_data['email'],
            password_hash=generate_password_hash(user_data['password'])
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def update_user(user_id, user_data):
        user = User.query.get(user_id)
        if not user:
            return None
            
        if 'username' in user_data:
            user.username = user_data['username']
        if 'email' in user_data:
            user.email = user_data['email']
        if 'password' in user_data:
            user.password_hash = generate_password_hash(user_data['password'])
            
        db.session.commit()
        return user
    
    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return False
            
        db.session.delete(user)
        db.session.commit()
        return True