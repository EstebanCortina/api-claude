from datetime import datetime

class User:
    def __init__(self, id=None, username=None, email=None, password_hash=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f'<User {self.username}>'