from flask import Blueprint
from auth.routes import init_routes

def create_auth_blueprint(service,url_prefix="/auth"):
    bp = Blueprint("auth",__name__,url_prefix=url_prefix)
    init_routes(bp,service)
    return bp