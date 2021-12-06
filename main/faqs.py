from flask import Blueprint
from flask import render_template, request, redirect

faqs_bp = Blueprint('faqs', __name__)


@faqs_bp.route('/faqs')
def get_docs():
    return render_template('faqs.html')
