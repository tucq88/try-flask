from flask_restful import Api, Resource


class AppApi(Api):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AppResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
