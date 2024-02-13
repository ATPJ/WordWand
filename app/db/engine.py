import os

from typing import Generator

from sqlmodel import SQLModel, create_engine, Session

# should import all models.
# from schemas.name import ModelName


db_conf = {
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
    "db_user": os.environ.get("DB_USER"),
    "db_password": os.environ.get("DB_PASSWORD"),
    "db_name": os.environ.get("DB_NAME")
}

URL = f"postgresql+psycopg2://{db_conf['db_user']}:{db_conf['db_password']}@ \
                              {db_conf['host']}:{db_conf['port']} \
                             /{db_conf['db_name']}"

engine = create_engine(URL)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def create_all():
    SQLModel.metadata.create_all(engine)
