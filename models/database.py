# pylint: disable= missing-docstring
from models.users import Users
from models.tasks import Tasks
from session import session


class SQLDatabase:
    def create_user(self, name: str, surname: str, username: str, password: str):
        user_data = Users(
            name=name, surname=surname, username=username, password=password
        )
        session.add(user_data)
        session.commit()

    def get_user(self, username: str):
        user = session.query(Users).filter_by(username=username).one()
        return user

    def get_user_id(self, username: str):
        user = session.query(Users).filter_by(username=username).one()
        return user.id

    def add_task(self, task: str, description: str, user_id: int) -> None:
        task = Tasks(task_name=task, task_desc=description, user_id=user_id)
        session.add(task)
        session.commit()

    def get_task(self, task_id: int):
        return session.query(Tasks).get(task_id)

    def get_all_tasks(self, user_id: int):
        all_tasks = session.query(Tasks).filter_by(user_id=user_id)
        return all_tasks

    def update_task(self, task_id: int, update_task: str, update_desc: str) -> None:
        task = self.get_task(task_id=task_id)
        task.task_name = update_task
        task.task_desc = update_desc
        session.commit()

    def delete_task(self, task_id: int) -> None:
        task = session.query(Tasks).get(task_id)
        session.delete(task)
        session.commit()
