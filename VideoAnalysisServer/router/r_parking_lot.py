from flask import Blueprint
from services import parking_lot


bp = Blueprint("index", __name__, url_prefix="/")

@bp.route("/ping", methods=["GET"])
def ping():
    """
    서버 상태 확인 용
    :return:
    """
    return "pong"


@bp.route("/parking_info", methods=["GET"])
def parking_info():
    """
    주차장 정보를 반환
    :return:
    """
    return parking_lot.parking_info()