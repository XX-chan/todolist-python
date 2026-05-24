from flask import Blueprint
from todo.routes import init_routes

# 创建todo蓝图
def create_todo_blueprint(service,url_prefix="/todo"):
    bp = Blueprint("todo",__name__,url_prefix=url_prefix)
    init_routes(bp,service)
    return bp