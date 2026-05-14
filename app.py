from flask import Flask, request,render_template,redirect,url_for,session
import sys
import os
from werkzeug.security import generate_password_hash, check_password_hash

# 把src提升为根目录
BASE_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(BASE_DIR, "src"))

from store.SqliteTodoStore import SqliteTodoStore
from store.SqliteUserStore import SqliteUserStore
from src.model.user import User
from src.service.todo_service import TodoService

app = Flask(__name__)

store = SqliteTodoStore()
service = TodoService(store)

user_store = SqliteUserStore()

app.secret_key = "你的随机密钥"

# 装饰器，当浏览器访问/首页时，调用home(),
@app.route("/")
def home():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    todos=service.get_user_todos(user_id)
    todos_sorted = sorted(todos,key=lambda t:t.completed)
    return render_template("index.html", todos = todos_sorted)

# 注册
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        password_hash = generate_password_hash(password)
        user = User(user_id=None, username=username, password_hash=password_hash)
        user_store.add(user)  # 用户保存到数据库
        return redirect(url_for("login"))
    return render_template("register.html")


# 登录
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        user = user_store.get_by_username(username)
        if user and check_password_hash(user.password_hash,password):
            session["user_id"]=user.user_id   # 记住这个用户已经登录。
            return redirect(url_for("home"))
        else:
            return "用户名或密码错误"
    return render_template("login.html")


# 登出
@app.route("/logout")
def logout():
    session.pop("user_id",None)
    return redirect(url_for("login"))


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    user_id = session.get("user_id")
    service.add(title,user_id)
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    user_id = session.get("user_id")
    service.remove(todo_id,user_id)
    return redirect(url_for("home"))


@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    user_id = session.get("user_id")
    service.complete(todo_id,user_id)
    return redirect(url_for("home"))


@app.route("/edit/<int:todo_id>")
def edit_page(todo_id):
    todo=store.find_todo(todo_id)
    return render_template("edit.html",todo=todo)


@app.route("/edit/<int:todo_id>",methods=["POST"])
def edit(todo_id):
    title=request.form.get("title")
    user_id = session.get("user_id")
    service.edit(todo_id,title,user_id)
    return redirect(url_for("home"))

# 确保只有直接运行这个文件时才能执行内部代码，import无效。
if __name__ == "__main__":
    app.run(debug=True)