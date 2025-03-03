import unittest
from app import create_app, db
from app.models import User

class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_create_user(self):
        user = User(username='test', email='test@example.com', password_hash='hash')
        db.session.add(user)
        db.session.commit()
        
        saved_user = User.query.filter_by(username='test').first()
        self.assertIsNotNone(saved_user)
        self.assertEqual(saved_user.email, 'test@example.com')
        
if __name__ == '__main__':
    unittest.main()