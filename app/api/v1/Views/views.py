from flask import Flask, Blueprint
version_1 = Blueprint("version_1", __name__, url_prefix="/api/v1/")