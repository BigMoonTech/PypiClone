import flask

from pypi_org.infrastructure.view_modifiers import response
from pypi_org.viewmodels.shared.viewmodel_base import ViewModelBase

blueprint = flask.Blueprint('sponsors', __name__, template_folder='templates')


@blueprint.route('/sponsors')
@response(template_file='sponsors/sponsors.html')
def sponsors():
    viewmodel = ViewModelBase()
    return viewmodel.to_dict()
