from flask import Flask


def create_app():
    app = Flask(__name__)

    from .v1 import bp_v1
    app.register_blueprint(bp_v1, url_prefix='/api/v1')

    return app
