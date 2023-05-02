from models.tasks import Tasks
from models.auth import Authentication
from models.database import SQLDatabase
from session import session

sql = SQLDatabase()
logged_in = False
while logged_in is False:
    print("Select action: \n1 - Sign up \n2 - Log in")
    choice = int(input("Your selection: "))
    if choice == 1:
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        sql.create_user(name, surname, username, password)
        auth = Authentication()
        logged_in = auth.check_auth(username, password)

    if choice == 2:
        print("Enter user name login information")
        username = input("Username: ")
        password = input("Password: ")
        auth = Authentication()
        logged_in = auth.check_auth(username, password)

    while logged_in is True:
        user = sql.get_user(username)
        print(
            "Select action: \n1 - View my tasks \n2 - Add task \n3 - Update task \n4 - Delete task \n5 - Exit"
        )
        choice = int(input("Your selection: "))
        if choice == 1:
            all_tasks = session.query(Tasks).filter_by(user_id=user.id)
            print(user.id)
            print("-------------------")
            for task in all_tasks:
                print(task)
            print("-------------------")

        if choice == 2:
            task_name = input("Task: ")
            task_desc = input("Description: ")
            task_data = Tasks(task_name=task_name, task_desc=task_desc, user_id=user.id)
            session.add(task_data)
            session.commit()

        if choice == 3:
            all_tasks = session.query(Tasks).filter_by(user_id=user.id)
            print("-------------------")
            for task in all_tasks:
                print(task)
            print("-------------------")
            selected_task_id = int(input("Select task ID: "))
            select_to_update = session.query(Tasks).get(selected_task_id)
            update_task = input("New task name: ")
            update_desc = input("New task description: ")
            user.tasks[0].task_name = update_task
            user.tasks[0].task_desc = update_desc
            session.commit()

        if choice == 4:
            all_tasks = session.query(Tasks).filter_by(user_id=user.id)
            print("-------------------")
            for task in all_tasks:
                print(task)
            print("-------------------")
            selected_task_id = int(input("Select task ID: "))
            select_to_delete = session.query(Tasks).get(selected_task_id)
            session.delete(select_to_delete)
            session.commit()

        if choice == 5:
            break
