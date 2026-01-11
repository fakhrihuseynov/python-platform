from flask import Blueprint, request, render_template, jsonify
from core.practice import run_practice
import json

bp = Blueprint("practice", __name__)

@bp.route("/", methods=["GET", "POST"])
def practice():
    result = None
    code = ""
    if request.method == "POST":
        code = request.form.get("code", "")
        user_inputs_json = request.form.get("user_inputs", None)
        
        user_inputs = None
        if user_inputs_json:
            user_inputs = json.loads(user_inputs_json)
        
        result = run_practice(code, user_inputs)
    return render_template("practice.html", result=result, code=code)
