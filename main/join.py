from flask import Blueprint
from flask import render_template, request, redirect

join_bp = Blueprint('join', __name__)


# 회원가입 api
@join_bp.route("/join")
def join():
    return render_template("join.html")
