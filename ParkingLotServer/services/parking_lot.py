from flask import current_app, jsonify
from sqlalchemy import text


def parking_info():
    """
    주차장 정보 반환
    :return:
    """

    rows = current_app.database.execute(text("""
        SELECT * FROM status
    """)).fetchall()

    parking_info = [{
        'lot_number': row['lot_number'],
        'status': row['status']
    } for row in rows]
    return jsonify(parking_info)


def parking_book(lot_number):
    pass


def parking_unbook(lot_number):
    pass
