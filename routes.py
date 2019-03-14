from app.common.api import AppApi
from app.views.posts import Posts


def register_routes(app):
    """
    Work around to avoid flask_restful override handle error exception
    https://github.com/flask-restful/flask-restful/issues/280
    """
    handle_exception = app.handle_exception
    handle_user_exception = app.handle_user_exception

    # Register routes
    api = AppApi(app)
    api.add_resource(Posts, '/')

    app.handle_exception = handle_exception
    app.handle_user_exception = handle_user_exception
