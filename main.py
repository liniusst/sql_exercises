from sqlalchemy import create_engine
from db.base import Base

engine = create_engine("sqlite:///db/to_do_task.db")
Base.metadata.create_all(engine, checkfirst=True)
