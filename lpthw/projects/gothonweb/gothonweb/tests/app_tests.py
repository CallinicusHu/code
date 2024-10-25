from lpthw.projects.gothonweb.gothonweb import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert (rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert (rv.status_code, 200)
    assert (b"Fill Out This Form", rv.data)

    data = ('name': 'Zed', 'greet': 'Hola')
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert (b"Zed", rv.data)
    assert (b"Hola", rv.data)
