from flask import Blueprint
from flask import render_template, request, redirect

about_bp = Blueprint('about', __name__)


@about_bp.route('/about')
def get_docs():
    return render_template('about.html')
