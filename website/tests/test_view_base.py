from app import client


def test_view_index():
    res = client.get('/')
    assert res.status_code == 200


def test_view_profile():
    res = client.get('/profile')
    assert res.status_code == 200
