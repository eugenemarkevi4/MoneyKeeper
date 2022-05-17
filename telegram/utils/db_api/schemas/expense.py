from sqlalchemy import Column, BigInteger, String, sql, Float

from telegram.utils.db_api.db_gino import TimedBaseModel, db

class Expense(TimedBaseModel):
    __tablename__ = "transactions_expenses"
    id = Column(BigInteger, primary_key=True)
    name_expenses = Column(String(100))
    account_id = Column(BigInteger)
    category_expenses_id = Column(BigInteger)
    img = Column(String)
    note = Column(String(100))
    status = Column(String(100))
    summ_expenses = Column(Float)
    tag_id = Column(BigInteger)
    user_id = Column(BigInteger)

    query: sql.select

# class Expense(TimedBaseModel):
#     __tablename__ = "users"
#     id = Column(BigInteger, primary_key=True)
#     name_expense = Column(String(100), primary_key=True)
#     category_expense = Column(String(100))
#     summ_expense = Column(BigInteger, primary_key=True)
#     tag_expense = Column(String(100))
#     account = Column(String(100))
#
#     query: sql.select