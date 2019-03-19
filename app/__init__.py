from flask_restful import Resource, Api
from flask import Flask, make_response
from flask_jwt_extended import JWTManager
from instances.config import app_config
from flask_cors import CORS
from app.api.v1.Views.views import version_1 as v1
#from app.api.v2.views.votes_views import version_2 as v2
from app.api.v2.views.offices_views import officee as officee
from app.api.v2.views.parties_views import party_version_2 as party_version_2
from app.api.v2.views.votes_views import votee as votee
from app.api.v2.views.candidate_views import candidatee as candidatee
from app.api.v2.views.nomination_views import nomination as nomination
from app.api.v2.views.result_views import result as result
from app.api.v2.views.authenticate import auth as auth 
from error_handlers import page_not_found, page_500
from app.api.v2.database.database_config import Connection



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.app_context().push()
    Connection().create_tables()
    #Connection().default_admin()
    CORS(app)
    app.config['SECRET_KEY'] = "sweet_secret"
    app.config['JWT_SECRET_KEY'] = "jwt_sweet_secret"
    app = Flask(__name__)
    app.register_blueprint(v1, url_prefix=("/api/v1"))
    app.register_blueprint(auth, url_prefix=("/api/v2"))
    app.register_blueprint(officee, url_prefix=("/api/v2"))
    app.register_blueprint(party_version_2, url_prefix=('/api/v2'))
    app.register_blueprint(votee, url_prefix=('/api/v2'))
    app.register_blueprint(candidatee, url_prefix=('/api/v2'))
    app.register_blueprint(nomination, url_prefix=('/api/v2'))
    app.register_blueprint(result, url_prefix=('/api/v2'))
    
    
    
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, page_500)
    jwt = JWTManager(app)

    @jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        return {
            'isAdmin': identity
        }

    return app
