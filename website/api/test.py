import requests

MAIN_URL = "http://127.0.0.1:5000/"


class TestMainPage:
    @staticmethod
    def test_get():
        response = requests.get(MAIN_URL)
        print(response.json())
        assert response.status_code == 200


class TestProfile:
    def __init__(self):
        pass
