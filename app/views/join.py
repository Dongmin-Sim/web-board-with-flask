from flask import render_template, make_response
from flask_restful import Resource


# Join api
class Join(Resource):
    def get(self):
        return make_response(render_template('join.html'))
