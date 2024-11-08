# :-(
#import sys
#sys.path.append('..')
#from lpthw.projects.gothonweb.gothonweb.src.app import index
from lpthw.projects.gothonweb.gothonweb.app import index


#app.config['TESTING'] = True
#web = app.test_client()

print(index)

"""def test_index():
    rv = web.get('/', follow_redirects=True)
    assert (rv.status_code == 404)

    rv = web.get('/hello', follow_redirects=True)
    assert (rv.status_code == 200)
    assert (b"Fill Out This Form" in rv.data)

    data = {'name': 'Zed', 'greet': 'Hola'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert (b"Zed" in rv.data)
    assert (b"Hola" in rv.data)
"""