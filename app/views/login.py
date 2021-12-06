from flask import render_template, make_response
from flask_restful import Resource


# Login api
class Login(Resource):
    def get(self):
        return make_response(render_template('login.html'))
