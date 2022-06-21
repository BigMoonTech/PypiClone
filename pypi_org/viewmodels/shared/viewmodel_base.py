from typing import Optional

import flask
from flask import Request
import pypi_org.infrastructure.request_dict as request_dict
import pypi_org.infrastructure.cookie_auth as cookie_auth
from pypi_org.services import user_service


class ViewModelBase:
    def __init__(self):
        self.request: Request = flask.request
        self.request_dict = request_dict.create('')
        self.error: Optional[str] = None
        self.user_id: Optional[int] = cookie_auth.get_user_id_via_auth_cookie(self.request)
        self.user: Optional[str] = user_service.find_user_by_id(self.user_id)

    def to_dict(self) -> dict:
        return self.__dict__
