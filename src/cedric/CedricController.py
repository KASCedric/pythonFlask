from flask import request, Blueprint

from src import db
from src.cedric.Cedric import Cedric
from src.utils.alchemyResponse import alchemy_response

bp = Blueprint("cedric", __name__, url_prefix="/api/cedric")


@bp.route('/addCedric', methods=['POST'])
def add_cedric():

    """Add a new cedric to db."""

    request_data = request.get_json()
    cedric = Cedric.from_json(request_data)

    if request_data['id']:
        db.session.query(Cedric).filter_by(id=request_data['id']).update(
            {column: getattr(cedric, column) for column in Cedric.__table__.columns.keys()})
        db.session.commit()
    else:
        db.session.add(cedric)  # Add new User record to database
        db.session.commit()  # Commit all changes

    return request_data


@bp.route('/getAllCedric', methods=['GET'])
def get_all_cedric():

    """Get all cedric from db."""

    response = Cedric.query.all()
    print(response)

    return alchemy_response(response)


@bp.route('/getCedricById/<id>', methods=['GET'])
def get_cedric_by_id(id_to_get):

    """get cedric by id from db."""

    response = Cedric.query.filter(Cedric.id == id_to_get).all()

    return alchemy_response(response)


@bp.route('/deleteAllCedric', methods=['GET'])
def delete_all_cedric():

    """delete all cedric from db."""

    response = Cedric.query.delete()
    db.session.commit()

    return alchemy_response(response)


@bp.route('/deleteCedricById/<id>', methods=['GET'])
def delete_cedric_by_id(id_to_delete):

    """delete cedric by id from db."""

    response = Cedric.query.filter(Cedric.id == id_to_delete).delete()
    db.session.commit()

    return alchemy_response(response)
