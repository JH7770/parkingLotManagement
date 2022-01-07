from flask import Flask, jsonify
from config import *


def register_router(app: Flask) -> Flask:
    """
    app에 router blueprints 등록
    :param app: Flask app
    :return: Flask app
    """
    from router import Blueprints

    for bp in Blueprints:
        app.register_blueprint(bp)

    return app


def create_app() -> Flask:
    """
    Flask app 생성 후 설정 하여 반환
    :return: Flask app
    """
    app = Flask(__name__)
    app = register_router(app)

    return app
