from flask import Blueprint

api = Blueprint("api", __name__)

from . import views, cards_goods, game_socket, game