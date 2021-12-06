from re import A
from flask import Blueprint
from flask.scaffold import F
from flask_restful import Resource, Api

from .main import Main
from .board import Board
from .about import About
from .docs import Docs
from .faqs import Faqs
from .join import Join
from .login import Login

app_views = Blueprint('app_views', __name__)
api = Api(app_views)

api.add_resource(Main, '/')
api.add_resource(About, '/about')
api.add_resource(Board, '/board')
api.add_resource(Docs, '/docs')
api.add_resource(Faqs, '/faqs')
api.add_resource(Join, '/join')
api.add_resource(Login, '/login')
