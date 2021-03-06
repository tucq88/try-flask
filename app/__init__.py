import json
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from routes import register_routes
from logs import register_logging

# For import *
# __all__ = ['Bootstrap']


class Bootstrap:
    app = None

    def __init__(self, app_name=__name__):
        load_dotenv()
        self.app = Flask(app_name, instance_relative_config=True)
        self.app.url_map.strict_slashes = False
        CORS(self.app)

        register_routes(self.app)
        register_logging(self.app)
        self._configure_error_handlers()

    def _configure_error_handlers(self):
        @self.app.errorhandler(500)
        def server_error_page(error):
            return json.dumps({'error': 'Internal server error'}), 500

        @self.app.errorhandler(404)
        def page_not_found(error):
            return json.dumps({'error': 'Resource not found'}), 404

    def instance(self):
        return self.app
