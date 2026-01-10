from flask import Blueprint, request, render_template
from core.practice import run_practice

bp = Blueprint("practice", __name__)

@bp.route("/", methods=["GET", "POST"])
def practice():
    result = None
    code = ""
    if request.method == "POST":
        code = request.form.get("code", "")
        result = run_practice(code)
    return render_template("practice.html", result=result, code=code)
