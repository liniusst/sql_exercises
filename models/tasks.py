from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    task_name = Column("Task", String)
    task_desc = Column("Description", String)
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("Users", back_populates="tasks")

    def __repr__(self):
        return f"[ID: {self.id}], Task: {self.task_name} Description: {self.task_desc}"
