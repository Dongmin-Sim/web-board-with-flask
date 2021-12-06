from flask import make_response, render_template
from flask_restful import Resource


# main api
class Main(Resource):
    def get(self):
        return make_response(render_template('main.html'))
