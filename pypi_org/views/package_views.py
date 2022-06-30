import flask
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.viewmodels.packages.packages_viewmodel import PackagesViewModel

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name: str):
    view_model = PackagesViewModel(package_name)
    view_model.validate()

    if view_model.error:
        return flask.abort(status=404)

    if view_model.package.releases:
        view_model.latest_release = view_model.package.releases[0]
        view_model.latest_version = view_model.latest_release.version_text

    return view_model.to_dict()


@blueprint.route('/<int:rank>')
def popular_packages(rank: int):
    return "Package details for the {}th most popular package".format(rank)
