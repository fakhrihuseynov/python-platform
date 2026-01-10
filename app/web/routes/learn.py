from flask import Blueprint, render_template
from core.lessons import get_lessons

bp = Blueprint("learn", __name__)

@bp.route("/")
def list_lessons():
    lessons = get_lessons()
    return render_template("learn.html", lessons=lessons)
