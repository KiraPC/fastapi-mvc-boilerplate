from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

from utils.db_connection import engine

Base = declarative_base()

class SampleObject(Base):
    # the name of the DB Table
    __tablename__ = "SampleTable"

    id = Column(String, primary_key=True, index=True)

# Create the table on DB automatically, when this class is loaded
Base.metadata.create_all(bind=engine)
