from flask import request,session,jsonify,render_template,redirect,url_for


# 此模块按业务分，负责：login、register、logout

# service 实例对象由外部传入。
def init_routes(bp,service):

    # 注册
    @bp.route("/register", methods=["GET", "POST"])
    def register():
        if request.method=="POST":
            username = request.form["username"]
            password = request.form["password"]
            result =  service.register(username,password)
            return redirect(url_for(result))
        return render_template("register.html")


    # 登录
    @bp.route("/api/login", methods=["POST"])
    def login():
        username = request.json["username"]
        password = request.json["password"]
        result = service.login(username,password)
        if result:
            session["user_id"]=result.user_id   # 后端创建session。
            return jsonify({
                "success":True,
                "message":"登陆成功"
            })
        else:
            return jsonify({
                "success":False,
                "message":"用户名或密码错误"
            }),401

    @bp.route("/login")
    def login_page():
        return render_template("login.html")


    # 登出
    @bp.route("/logout")
    def logout():
        session.pop("user_id",None)
        return redirect(url_for("login_page"))
