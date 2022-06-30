from pypi_org.viewmodels.shared.viewmodel_base import ViewModelBase
from pypi_org.services import package_service
import flask


class SitemapViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.packages = package_service.all_packages()
        self.last_updated_text = '2022-06-30'
        self.site = f'{flask.request.scheme}://{flask.request.host}'
