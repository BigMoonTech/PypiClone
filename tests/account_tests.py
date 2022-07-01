from flask import Response
from test_client import flask_app
from pypi_org.data.users import User
import unittest.mock

def test_viewmodel_register_validation_is_passed():
    from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel

    form_data = {
        'name': 'Joshua',
        'email': 'joshraguilar@gmail.com',
        'password': '123456'
    }

    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    target = 'pypi_org.services.user_service.find_user_by_email'

    with unittest.mock.patch(target, return_value=None):
        vm.validate()

    assert vm.error is None


def test_viewmodel_register_user_already_exists():
    from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel

    form_data = {
        'name': 'Joshua',
        'email': 'joshraguilar@gmail.com',
        'password': '123456'
    }

    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    target = 'pypi_org.services.user_service.find_user_by_email'
    test_user = User(email=form_data.get('email'))
    with unittest.mock.patch(target, return_value=test_user):
        vm.validate()

    assert vm.error is not None
    assert 'already exists' in vm.error


def test_view_register_successful_and_redirect_to_account_view():
    from pypi_org.views.account_views import register_post
    form_data = {
        'name': 'Joshua',
        'email': 'joshraguilar@gmail.com',
        'password': '123456'
    }

    target = 'pypi_org.services.user_service.find_user_by_email'
    find_user = unittest.mock.patch(target, return_value=None)
    target = 'pypi_org.services.user_service.create_user'
    create_user = unittest.mock.patch(target, return_value=User())
    request = flask_app.test_request_context(path='/account/register', data=form_data)

    with find_user, create_user, request:
        resp: Response = register_post()

    assert resp.location == '/account'


def test_integration_account_page_not_logged_in_redirect_to_login(client):
    target = 'pypi_org.services.user_service.find_user_by_id'
    with unittest.mock.patch(target, return_value=None):
        resp: Response = client.get('/account')

    assert resp.status_code == 302
    assert resp.location == '/account/login'


def test_integration_account_page_logged_in(client):
    target = 'pypi_org.services.user_service.find_user_by_id'
    test_user = User(name='Joshua', email='joshraguilar@gmail.com')
    with unittest.mock.patch(target, return_value=test_user):
        resp: Response = client.get('/account')

    assert resp.status_code == 200
    assert b'Joshua' in resp.data
