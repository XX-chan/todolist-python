from flask import Blueprint,url_prefix
from auth.blueprint import init_routes

def creat_auth_blueprint(service,url_prefix="/auth"):
    bp = Blueprint("auth",__name__,url_prefix=url_prefix)
    init_routes(bp,service)
    return bp