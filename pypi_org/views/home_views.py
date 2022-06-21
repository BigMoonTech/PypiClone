import flask

from pypi_org.infrastructure.view_modifiers import response
from pypi_org.viewmodels.home.home_viewmodel import HomeViewModel

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    viewmodel = HomeViewModel()
    return viewmodel.to_dict()
    # return flask.render_template('home/index.html', packages=test_packages)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    viewmodel = HomeViewModel()
    return viewmodel.to_dict()
