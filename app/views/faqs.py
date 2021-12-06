from flask import render_template, make_response
from flask_restful import Resource


# FAQs api
class Faqs(Resource):
    def get(self):
        return make_response(render_template('faqs.html'))
