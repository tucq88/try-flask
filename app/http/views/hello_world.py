from app.common.api import AppResource


class HelloWorld(AppResource):
    def get(self):
        return {'hello': 'world'}
