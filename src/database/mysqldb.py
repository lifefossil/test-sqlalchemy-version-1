from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from src.core.config import mysql_config as config

mysql_url: str = rf'mysql+mysqldb://{config.username}:{config.password}@{config.host}:{config.port}/{config.database}'
engine = create_engine(mysql_url, echo=True, future=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

if __name__ == '__main__':
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print()
