import json

from flask import make_response

from src.utils.alchemyEncoder import AlchemyEncoder


def alchemy_response(data):
    return make_response(json.dumps(data, cls=AlchemyEncoder))
