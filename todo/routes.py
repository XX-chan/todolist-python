from flask import Blueprint,session,jsonify,render_template,redirect,url_for,request

def init_routes(bp,service):

    # 数据接口
    @bp.route("/api/todos")
    def api_todos():
        user_id = session.get("user_id")
        result = service.get_user_todos_dict(user_id)
        return jsonify(result)


    # 首页：返回 HTML 壳页面；待办数据由 /api/todos 提供
    @bp.route("/")
    def home():
        if not session.get("user_id"):
            return redirect(url_for("auth.login_page"))
        return render_template("index.html")



    @bp.route("/add", methods=["POST"])
    def add():
        title = request.json.get("title")
        user_id = session.get("user_id")
        service.add(title,user_id)
        return jsonify({
            "success":True
        })


    @bp.route("/delete/<int:todo_id>",methods=["DELETE"])
    def delete(todo_id):
        user_id = session.get("user_id")
        service.remove(todo_id,user_id)
        return jsonify({
            "success":True
        })


    @bp.route("/complete/<int:todo_id>",methods=["POST"])
    def complete(todo_id):
        user_id = session.get("user_id")
        service.complete(todo_id,user_id)
        return jsonify({
            "success":True
        })


    @bp.route("/edit/<int:todo_id>")
    def edit_page(todo_id):
        return render_template("edit.html")

    @bp.route("/api/todo/<int:todo_id>")
    def get_todo(todo_id):
        todo=service.store.find_todo(todo_id)
        return jsonify({
            "todo_id":todo.todo_id,
            "title":todo.title,
            "completed":todo.completed
        })


    @bp.route("/edit/<int:todo_id>",methods=["PUT"])
    def edit(todo_id):
        title=request.json.get("title")
        user_id = session.get("user_id")
        service.edit(todo_id,title,user_id)
        return jsonify({
            "success":True
        })
    
    
