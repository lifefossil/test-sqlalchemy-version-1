from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from src.database.mysqldb import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(16), unique=True)
    password = Column(String(16))
    user_type = Column(Integer, default=100, comment="用户类型, 0:超级管理员, 100:普通用户, 200:vip用户")
    is_active = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())
