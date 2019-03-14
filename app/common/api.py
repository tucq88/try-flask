from flask_restful import Api, Resource
from flask import _app_ctx_stack
from sqlalchemy.orm import scoped_session
from database import Session

Session = scoped_session(Session, scopefunc=_app_ctx_stack.__ident_func__)


class AppApi(Api):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AppResource(Resource):

    session = Session()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
