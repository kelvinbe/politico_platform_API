from flask import Flask
from app.api.v1.Views.views import version_1 as v1
from error_handlers import page_not_found, page_500

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(v1, url_prefix=("/api/v1/"))

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, page_500)

    return app


