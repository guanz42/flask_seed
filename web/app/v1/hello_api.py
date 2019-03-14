from flask import current_app
from flask_restful import Resource

from app.v1 import api_v1


@api_v1.resource('/hello')
class HelloWorld(Resource):
    def get(self):
        current_app.logger.debug('debug log')
        current_app.logger.info('info log')
        current_app.logger.error('error log')
        return {"hello": "world"}
