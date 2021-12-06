from flask import render_template, make_response
from flask_restful import Resource


# about api
class About(Resource):
    def get(self):
        return make_response(render_template('about.html'))
