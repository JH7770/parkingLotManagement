from sqlalchemy import create_engine, text
from config import DB_URL

class DBHandler:
    def __init__(self):
        self.database = create_engine(DB_URL, encoding='utp-8', max_overflow=0)

