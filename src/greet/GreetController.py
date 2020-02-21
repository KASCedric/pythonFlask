from flask import Blueprint, request

bp = Blueprint("greet", __name__, url_prefix="/api/greet")


def say_hello(username="World"):
    return 'Hello %s!\n' % username


@bp.route('/')
def index():
    return say_hello()


@bp.route('/hello/<username>')
def hello(username):
    return say_hello(username)


@bp.route('/json-example', methods=['POST'])
def json_example():
    return request.get_json()
