from app import client

MAIN_DATA = ['AlexBob', 'gaerpt2ip5j23p']


def test_view_registration():
    res = client.get('/registration')
    assert res.status_code == 200

    data = {
        'username': MAIN_DATA[0],
        'password1': MAIN_DATA[1],
        'password2': MAIN_DATA[2],
    }

    res = client.post('/registration', json=data)
    assert res.status_code == 200

    data = {
        'username': MAIN_DATA[0],
        'password1': MAIN_DATA[1],
        'password2': 'gakdofg3333',
    }

    res = client.post('/registration', json=data)
    assert res.status_code == 404


def test_view_login():
    res = client.get('/login')
    assert res.status_code == 200

    data = {
        'username': MAIN_DATA[0],
        'password': MAIN_DATA[1]
    }
    res = client.post('/login', json=data)
    assert res.status_code == 200


def test_view_logout():
    res = client.get('/logout')
    assert res.status_code == 200
