import os

try:
    DB_USER = os.environ.get("DB_USER_NAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_POST")
    DB_NAME = os.environ.get("DB_NAME")

    DB_URL = DB_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8"
except Exception as e:
    print("Database Environmental variable error : ", e)
    exit(-1)





