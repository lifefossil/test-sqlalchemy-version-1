from src.database.mysqldb import engine
from src.model import Base, User
from src.service import user_service

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    user = User()
    user.username = 'oliver'
    user.password = '123456'
    user = user_service.create_user(user)
