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
        self.datat = {
            "id": 1,
            "name": "barno",
            "logoUrl": "img.jpeg",
            "hqAddress": "uuu",
        }

    def post(self, path='/api/v1/parties', data={}):
        if not data:
            data = self.data

        resp = self.client.post(path='/api/v1/parties',
                                data=json.dumps(self.data), content_type='application/json')
        return resp



    def test_creating_a_party(self):
        resp = self.post()
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json['msg'], 'party created successfully')

    def test_get_all_parties(self):
        resp = self.client.get(path='/api/v1/parties',
                               content_type='appliction/json')
        self.assertEqual(resp.status_code, 200)

    def test_get_specific_party(self):
        post = self.post()
        path = '/api/v1/parties/1'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_edit_specific_party(self):
        post = self.client.post(path='/api/v1/parties', data=json.dumps(self.data), content_type='application/json')
        id = post.get_json()["data"]["id"]
        name = post.get_json('name')
        path = '/api/v1/parties/{}/name'.format(id)
        response = self.client.patch(path, data=json.dumps(self.datat), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_specific_party(self):
        post = self.client.post(path='/api/v1/parties', data=json.dumps(self.data), content_type='application/json')
        id = post.get_json()["data"]["id"]
        path = '/api/v1/parties/{}'.format(id)
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        
        


   