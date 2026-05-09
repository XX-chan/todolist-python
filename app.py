from flask import Flask, request,render_template,redirect,url_for
import sys
import os

# 把src提升为根目录
BASE_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(BASE_DIR, "src"))

from src.store.sqlite_store import SqliteTodoStore
from src.service.todo_service import TodoService

app = Flask(__name__)

store = SqliteTodoStore()
service = TodoService(store)

# 装饰器，当浏览器访问/首页时，调用home(),
@app.route("/")
def home():
    todos=service.list()

    # render_template是Flask的函数，用于渲染模板
    # 当用户访问首页时，返回index.html 页面
    return render_template(
        "index.html",
        todos=todos)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if title:
        service.add(title)
    return redirect(url_for("home"))

# 确保只有直接运行这个文件时才能执行内部代码，import无效。
if __name__ == "__main__":
    app.run(debug=True)