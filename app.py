# pylint: disable= missing-docstring
from models.auth import Authentication
from models.database import SQLDatabase


db = SQLDatabase()
auth = Authentication()

while True:
    print("Select action: \n1 - Sign up \n2 - Log in \n3 - Exit")
    choice = int(input("Your selection: "))
    if choice == 1:
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        db.create_user(name, surname, username, password)
        status = auth.check_auth(username, password)

    if choice == 2:
        print("Enter user name login information")
        username = input("Username: ")
        password = input("Password: ")
        status = auth.check_auth(username, password)

    if choice == 3:
        break

    while status:
        user_id = db.get_user_id(username)
        print(
            "Select action: \n1 - View my tasks \n2 - Add task \n3 - Update task \n4 - Delete task \n5 - Exit"
        )
        choice = int(input("Your selection: "))
        if choice == 1:
            for task in db.get_all_tasks(user_id):
                print(task)

        if choice == 2:
            task_name = input("Task: ")
            task_desc = input("Description: ")
            db.add_task(task_name, task_desc, user_id)

        if choice == 3:
            for task in db.get_all_tasks(user_id):
                print(task)

            selected_task_id = int(input("Select task ID: "))
            update_task = input("New task name: ")
            update_desc = input("New task description: ")
            db.update_task(selected_task_id, update_task, update_desc)

        if choice == 4:
            for task in db.get_all_tasks(user_id):
                print(task)

            selected_task_id = int(input("Select task ID: "))
            db.delete_task(selected_task_id)

        if choice == 5:
            break
