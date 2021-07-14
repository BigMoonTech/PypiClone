import flask

app = flask.Flask(__name__)


def get_packages():
    return [
        {'name': 'flask', 'version': '1.2.3'},
        {'name': 'sqlalchemy', 'version': '2.0'},
        {'name': 'retard', 'version': '3.8'}
    ]


@app.route('/')
def index():
    test_packages = get_packages()
    return flask.render_template('home/index.html', packages=test_packages)


@app.route('/about')
def about():
    return flask.render_template('home/about.html')


if __name__ == '__main__':
    app.run()
