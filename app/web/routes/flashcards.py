from flask import Blueprint, render_template, request, redirect
from core.flashcards import load_due_cards, grade_card

bp = Blueprint("flashcards", __name__)

@bp.route("/", methods=["GET", "POST"])
def review():
    if request.method == "POST":
        card_id = request.form.get("card_id")
        grade = int(request.form.get("grade"))
        grade_card(card_id, grade)
        return redirect("/flashcards/")
    cards = load_due_cards()
    return render_template("flashcards.html", cards=cards)
