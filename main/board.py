from flask import Blueprint
from flask import render_template, request, redirect

board_bp = Blueprint('board', __name__)


# 게시판 영역 api
@board_bp.route("/board")
def post():
    return render_template("board.html")
