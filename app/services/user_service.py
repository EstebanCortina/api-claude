from werkzeug.security import generate_password_hash
from app.models import User
from datetime import datetime

class UserService:
    # In-memory storage
    users = []
    current_id = 1
    
    @classmethod
    def create_user(cls, user_data):
        # Check if username or email already exists
        for user in cls.users:
            if user.username == user_data['username']:
                return None, "Username already exists"
            if user.email == user_data['email']:
                return None, "Email already exists"
                
        user = User(
            id=cls.current_id,
            username=user_data['username'],
            email=user_data['email'],
            password_hash=generate_password_hash(user_data['password'])
        )
        cls.users.append(user)
        cls.current_id += 1
        return user, None

    @classmethod
    def get_user_by_id(cls, user_id):
        for user in cls.users:
            if user.id == user_id:
                return user
        return None
    
    @classmethod
    def get_all_users(cls):
        return cls.users
    
    @classmethod
    def update_user(cls, user_id, user_data):
        user = cls.get_user_by_id(user_id)
        if not user:
            return None
            
        # Check if new username or email already exists with another user
        if 'username' in user_data and user_data['username'] != user.username:
            for existing_user in cls.users:
                if existing_user.id != user_id and existing_user.username == user_data['username']:
                    return None
        
        if 'email' in user_data and user_data['email'] != user.email:
            for existing_user in cls.users:
                if existing_user.id != user_id and existing_user.email == user_data['email']:
                    return None
                    
        if 'username' in user_data:
            user.username = user_data['username']
        if 'email' in user_data:
            user.email = user_data['email']
        if 'password' in user_data:
            user.password_hash = generate_password_hash(user_data['password'])
            
        user.updated_at = datetime.utcnow()
        return user
    
    @classmethod
    def delete_user(cls, user_id):
        user = cls.get_user_by_id(user_id)
        if not user:
            return False
            
        cls.users.remove(user)
        return True