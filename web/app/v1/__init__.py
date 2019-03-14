from flask import Blueprint
from flask_restful import Api

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}

bp_v1 = Blueprint('api_v1', __name__)
api_v1 = Api(bp_v1, errors=errors)

from . import hello_api
