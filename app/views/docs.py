import re
from flask import render_template, make_response
from flask_restful import Resource


# docs api
class Docs(Resource):
    def get(self):
        return make_response(render_template('docs.html'))
