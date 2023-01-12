from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.database.mysqldb import engine
from src.model.user import User


def create_user(user: User) -> User | None:
    with Session(engine) as session:
        try:
            session.add(user)
            session.commit()
            session.flush(user)
            user.password = ''
            return user
        except IntegrityError as e:
            print(e.args)
            return None
