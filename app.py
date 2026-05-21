from flask import Flask, request,render_template,redirect,url_for,session,jsonify
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

# 数据接口
@app.route("/api/todos")
def api_todos():
    user_id = session.get("user_id")
    todos = service.get_user_todos(user_id)
    result = []

    for t in todos:
        result.append(t.to_dict())
        
    return jsonify(result)



# 首页：返回 HTML 壳页面；待办数据由 /api/todos 提供
@app.route("/")
def home():
    if not session.get("user_id"):
        return redirect(url_for("login_page"))
    return render_template("index.html")



# 注册
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        password_hash = generate_password_hash(password)
        user = User(user_id=None, username=username, password_hash=password_hash)
        user_store.add(user)  # 用户保存到数据库
        return redirect(url_for("login_page"))
    return render_template("register.html")


# 登录
@app.route("/api/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]
    user = user_store.get_by_username(username)
    if user and check_password_hash(user.password_hash,password):
        session["user_id"]=user.user_id   # 后端创建session。
        return jsonify({
            "success":True,
            "message":"登陆成功"
        })
    else:
        return jsonify({
            "success":False,
            "message":"用户名或密码错误"
        }),401

@app.route("/login")
def login_page():
    return render_template("login.html")


# 登出
@app.route("/logout")
def logout():
    session.pop("user_id",None)
    return redirect(url_for("login_page"))


@app.route("/add", methods=["POST"])
def add():
    title = request.json.get("title")
    user_id = session.get("user_id")
    service.add(title,user_id)
    return jsonify({
        "success":True
    })


@app.route("/delete/<int:todo_id>",methods=["DELETE"])
def delete(todo_id):
    user_id = session.get("user_id")
    service.remove(todo_id,user_id)
    return jsonify({
        "success":True
    })


@app.route("/complete/<int:todo_id>",methods=["POST"])
def complete(todo_id):
    user_id = session.get("user_id")
    service.complete(todo_id,user_id)
    return jsonify({
        "success":True
    })


@app.route("/edit/<int:todo_id>")
def edit_page(todo_id):
    return render_template("edit.html")

@app.route("/api/todo/<int:todo_id>")
def get_todo(todo_id):
    todo=store.find_todo(todo_id)
    return jsonify({
        "todo_id":todo.todo_id,
        "title":todo.title,
        "completed":todo.completed
    })


@app.route("/edit/<int:todo_id>",methods=["PUT"])
def edit(todo_id):
    title=request.json.get("title")
    user_id = session.get("user_id")
    service.edit(todo_id,title,user_id)
    return jsonify({
        "success":True
    })

# 确保只有直接运行这个文件时才能执行内部代码，import无效。
if __name__ == "__main__":
    app.run(debug=True)