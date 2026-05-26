from config import get_config
from flask import Flask,redirect

# 工厂模式
def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    from app.todo.store import SqliteTodoStore
    from app.auth.store import SqliteUserStore
    # 创建store
    user_store = SqliteUserStore(db_path=app.config["USER_DB_PATH"])
    todo_store = SqliteTodoStore(db_path=app.config["TODOS_DB_PATH"])

    from app.todo.service import TodoService
    from app.auth.service import AuthService
    # 创建service
    auth_service=AuthService(user_store)
    todo_service=TodoService(todo_store)

    from app.auth.blueprint import create_auth_blueprint
    from app.todo.blueprint import create_todo_blueprint
    # 创建蓝图i
    auth_bp = create_auth_blueprint(auth_service)
    todo_bp = create_todo_blueprint(todo_service)

    # 注册
    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)

    
    @app.route("/")
    def root():
        return redirect("/todo/")

    return app