from app_init import create_app

app = create_app()

@app.route("/ping", methods=["GET"])
def ping():
    """
    서버 상태 확인 용
    :return:
    """
    return "pong"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5678)