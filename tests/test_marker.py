from tests.baseTest import BaseTest
import json


class MarkerTest (BaseTest):

    def test_all(self):

        client_app = self.app
        response = client_app.get('/marker/all')
        assert not(response.data.decode("utf-8")) is True

        data = {
            'lat': 12,
            'lng': 13
        }
        # response = client_app.post("/marker/add", data=json.dumps(data))
        response = client_app.post("/marker/add", data=data)
        response = json.loads(response.data.decode("utf-8"))
        assert data['lat'] == int(response['lat'])
        assert data['lng'] == int(response['lng'])
        assert 1 == int(response['id'])
        assert "Adicionado com sucesso" in response['msg']

        response = client_app.get('/marker/all')
        assert not(response.data.decode("utf-8")) is False

    def test_add(self):
        client_app = self.app
        data = {
            'lat': 12,
            'lng': 13
        }
        # response = client_app.post("/marker/add", data=json.dumps(data))
        response = client_app.post("/marker/add", data=data)
        response = json.loads(response.data.decode("utf-8"))
        assert data['lat'] == int(response['lat'])
        assert data['lng'] == int(response['lng'])
        assert 1 == int(response['id'])
        assert "Adicionado com sucesso" in response['msg']
