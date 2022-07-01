from flask import Response
from tests.test_client import flask_app
from views import home_views


def test_home_page(client):
    resp: Response = client.get('/')
    assert resp.status_code == 200
    assert b'Find, install and publish Python packages' in resp.data


def test_home_page_directly():
    with flask_app.test_request_context(path='/'):
        resp: Response = home_views.index()

    assert resp.status_code == 200
    assert len(resp.model.get('releases')) > 0
