from flask import Flask,redirect


def create_app():
    app = Flask(__name__)
    app.secret_key = "你的随机密钥"

    from todo.store import SqliteTodoStore
    from auth.store import SqliteUserStore
    # 创建store
    user_store = SqliteUserStore()
    todo_store = SqliteTodoStore()

    from todo.service import TodoService
    from auth.service import AuthService
    # 创建service
    auth_service=AuthService(user_store)
    todo_service=TodoService(todo_store)

    from auth.blueprint import create_auth_blueprint
    from todo.blueprint import create_todo_blueprint
    # 创建蓝图i
    auth_bp = create_auth_blueprint(auth_service)
    todo_bp = create_todo_blueprint(todo_service)

    # 注册
    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)

    return app
# 创建Flask app
app=create_app()

@app.route("/")
def root():
    return redirect("/todo/")

# 只有被自己运行时才启动服务器
if __name__ == "__main__":
    app.run(debug=True)