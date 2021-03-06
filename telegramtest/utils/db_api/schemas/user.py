from sqlalchemy import Integer, Column, BigInteger, String, sql

from telegram.utils.db_api.db_gino import TimedBaseModel

class User(TimedBaseModel):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    first_name = Column(String(100))
    nick_name = Column(String(100))

    query: sql.Select