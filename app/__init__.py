from flask import Flask
from app.api.v1.Views.views import version_1 as v1


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(v1, url_prefix=("/api/v1/"))
    return app


