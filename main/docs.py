from flask import Blueprint
from flask import render_template, request, redirect

docs_bp = Blueprint('docs', __name__)


@docs_bp.route('/docs')
def get_docs():
    return render_template('docs.html')
