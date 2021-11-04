from flask import Blueprint
from flask import render_template, request, redirect

board = Blueprint('board', __name__)


@board.route("/", methods=['GET'])
def root():
    return render_template("index.html")


@board.route("/home")
def home():

    return render_template
