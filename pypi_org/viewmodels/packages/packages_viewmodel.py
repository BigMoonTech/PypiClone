from pypi_org.services import package_service
from pypi_org.viewmodels.shared.viewmodel_base import ViewModelBase


class PackagesViewModel(ViewModelBase):
    def __init__(self, package_name: str = None):
        super().__init__()

        self.package_name = package_name
        self.package = package_service.get_package_by_id(self.package_name)

        self.latest_release = '0.0.0'
        self.latest_version = None
        self.release_version = self.latest_release
        self.is_latest = True

    def validate(self):
        if not self.package_name or not self.package:
            self.error = 'Package not found.'
