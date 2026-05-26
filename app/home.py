from flask import redirect,Blueprint

bp=Blueprint("home",__name__)

@bp.route("/")
def root():
    return redirect("/todo/")