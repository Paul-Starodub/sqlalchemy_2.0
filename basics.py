from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import Session


# engine = create_engine("sqlite:///mydatabase.db", echo=True)
engine = create_engine("postgresql+psycopg://postgres:postgres@localhost:5432/satutorialdatabase", echo=True)
#
#
# conn = engine.connect()
#
# conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int)"))
# conn.commit()
#
#
# session = Session(engine)
#
# session.execute(text("INSERT INTO people (name, age) VALUES ('John', 30)"))
# session.commit()


metadata = MetaData()

people = Table(
    "people",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
)

metadata.create_all(engine)
