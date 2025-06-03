
import unittest
from main import app, db

class IdentifyTestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_create_first_contact(self):
        payload = {
            "email": "doc@flux.com",
            "phoneNumber": "1010101010"
        }
        response = self.app.post('/identify', json=payload)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['contact']['emails'], ["doc@flux.com"])
        self.assertEqual(data['contact']['phoneNumbers'], ["1010101010"])
        self.assertEqual(data['contact']['secondaryContactIds'], [])

if __name__ == '__main__':
    unittest.main()
    #  $env:PYTHONPATH="."; python test/test_identify.py
    
