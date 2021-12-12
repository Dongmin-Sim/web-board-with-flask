from flask import render_template, make_response
from flask_restful import Resource
from ..forms import LoginForm


# Login api
class Login(Resource):
    def get(self):
        form = LoginForm()
        return make_response(render_template('login.html', form=form))

    def post(self):
        form = LoginForm()
        return
