from flask_restful import Resource, Api
from flask import Flask
from app.api.v1.Views.views import version_1 as v1
from app.api.v2.views.votes_views import version_2 as v2
from app.api.v2.views.offices_views import offices as offices
from error_handlers import page_not_found, page_500



def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1, url_prefix=("/api/v1/"))
    app.register_blueprint(v2, url_prefix=("/api/v2/"))
    app.register_blueprint(offices, url_prefix=("/api/v2"))
    
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, page_500)

    return app
