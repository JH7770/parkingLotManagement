from flask import Blueprint
from services import parking_lot

bp = Blueprint("index", __name__, url_prefix="/parking")


@bp.route("/info", methods=["GET"])
def parking_info():
    """
    주차장 정보를 반환
    :return:
    """
    return parking_lot.parking_info()


@bp.route("/book/<int:lot_number>", methods=['POST'])
def parking_book(lot_number):
    """
    주차장 예약
    :param lot_number: 주차장 자리 번호
    :return:
    """
    return "", 200




@bp.route("/unbooking/<int:lot_number>", methods=['POST'])
def parking_unbook(lot_number):
    """
    주차장 예약 취소
    :param lot_number: 주차장 자리 번호
    :return:
    """
    return "", 200
