import json
import unittest
from run import create_app


class TestOfficeCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.data = {
            "id": 1,
            "name": "Presidency",
            "type": "img.png",
            
        }

    def post(self, path='/api/v1/offices', data={}):
        if not data:
            data = self.data

        resp = self.client.post(path='/api/v1/offices',
                                data=json.dumps(self.data), content_type='application/json')
        return resp

    def test_creating_a_office(self):
        resp = self.post()
        self.assertEqual(resp.status_code, 201)
        
