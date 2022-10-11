from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://postgres:Manjunath96@localhost:5432/Xvector")

meta = MetaData()
conn = engine.connect()
Base = declarative_base()
SessionLocal = sessionmaker(bind= engine, autocommit=False, autoflush=False)
# print (conn)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()