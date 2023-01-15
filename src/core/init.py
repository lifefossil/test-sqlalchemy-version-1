# 项目启动的时候初始化数据库
from src.database.mysqldb import Base, engine


def init_database():
    """
    初始化数据库
    检查表是否存在,不存在根据Model在数据库中创建表;
    如果存在则忽略
    :return:
    """
    # 检查表是否存在, 不存在根据Model在数据库中创建表
    Base.metadata.create_all(bind=engine)
