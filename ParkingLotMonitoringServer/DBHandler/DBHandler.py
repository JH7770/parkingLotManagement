from sqlalchemy import create_engine, text
from config import DB_URL

class DBHandler:
    def __init__(self):
        try:
            self.database = create_engine(DB_URL, encoding='utf-8', max_overflow=0)
        except Exception as e:
            print(e)
        finally:
            print("DB Connected")

    def insert(self, query):
        try:
            ret = self.database.execute(query)
        except Exception as e:
            print(e)
            return e
        return ret

    def update(self, query):
        try:
            ret = self.database.execute(query)
        except Exception as e:
            print(e)
            return e
        return ret