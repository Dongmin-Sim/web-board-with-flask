from flask import Blueprint
from flask import render_template, request, redirect

login_bp = Blueprint('login', __name__)


# 로그인 api
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        return
