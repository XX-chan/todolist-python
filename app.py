from flask import Flask,Blueprint, request,render_template,redirect,url_for,session,jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from auth.routes import create_auth_blueprint
from todo.routes import create_todo_blueprint
from todo.store import SqliteTodoStore
from auth.store import SqliteUserStore

from todo.service import TodoService
from auth.service import AuthService

def create_app():
    app = Flask(__name__)
    app.secret_key = "你的随机密钥"

    # 创建store
    user_store = SqliteUserStore()
    todo_store = SqliteTodoStore()

    # 创建service
    auth_service=AuthService(user_store)
    todo_service=TodoService(todo_store)

    # 创建蓝图i
    auth_bp = create_auth_blueprint(auth_service)
    todo_bp = create_todo_blueprint(todo_service)

    # 注册
    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)

    return app