import json
import unittest
from run import create_app


class TestPoliticoApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.data = {
            "id": 1,
            "name": "Kelvin",
            "logoUrl": "img.png",
            "hqAddress": "hhiii",
        }

    def post(self, path='/api/v1/parties', data={}):
        if not data:
            data = self.data

        resp = self.client.post(path='/api/v1/parties', 
        data=json.dumps(self.data),content_type='application/json')
        return resp

    def test_creating_a_party(self):
        resp = self.post()
        self.assertEqual(resp.status_code, 201)
        # self.assertTrue(resp.json['id'])
        self.assertEqual(resp.json['msg'], 'party created successfully')
 