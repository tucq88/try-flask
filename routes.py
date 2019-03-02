from flask_restful import Resource, Api
from app.http.views.hello_world import HelloWorld

handle_exception = ''
handle_user_exception = ''

def register_routes(app):
    # Work around to avoid flask_restful override handle error exception
    # https://github.com/flask-restful/flask-restful/issues/280
    _save_flask_default_handle_exception(app)

    # Register routes
    api = Api(app)
    api.add_resource(HelloWorld, '/')

    # Work around to avoid flask_restful override handle error exception
    # https://github.com/flask-restful/flask-restful/issues/280
    _load_flask_default_exception(app)

def _save_flask_default_handle_exception(app):
    handle_exception = app.handle_exception
    handle_user_exception = app.handle_user_exception

def _load_flask_default_exception(app):
    app.handle_exception = handle_exception
    app.handle_user_exception = handle_user_exception
