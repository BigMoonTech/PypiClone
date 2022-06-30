# noinspection PyUnresolvedReferences
import pypi_org.services.package_service
from tests.test_client import flask_app, client

from flask import Response
import unittest.mock
import datetime


def test_package_details_found_ok():
    from pypi_org.data.releases import Release
    from pypi_org.views.package_views import package_details
    from pypi_org.data.packages import Package

    test_package = Package()

    test_package.id = 'sqlalchemy'
    test_package.description = 'TBD'
    test_package.releases = [
        Release(created_date=datetime.datetime.now(), major_version=1, minor_version=2, build_version=200),
        Release(created_date=datetime.datetime.now() - datetime.timedelta(days=10))
    ]

    target01 = 'pypi_org.services.package_service.get_package_by_id'

    with unittest.mock.patch(target01, return_value=test_package):
        with flask_app.test_request_context(path='/project/' + test_package.id):
            resp: Response = package_details(test_package.id)

    assert b'sqlalchemy 1.2.200' in resp.data


def test_package_details_not_found_404(client):
    bad_package_url = 'project/sqlalchemy_superfuntime'
    target = 'pypi_org.services.package_service.get_package_by_id'
    with unittest.mock.patch(target, return_value=None):
        resp: Response = client.get(bad_package_url)

    assert resp.status_code == 404
