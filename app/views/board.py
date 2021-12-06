from flask import render_template, make_response
from flask_restful import Resource, Api

# board api


class Board(Resource):
    def get(self):
        return make_response(render_template('board.html'))
