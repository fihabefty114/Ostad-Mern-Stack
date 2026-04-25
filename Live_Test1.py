import json
import os

class TaskManager:
    def __init__(self):
        self.task = []
        self.f_name = "tasks.json"

    def load_task(self):
        if os.path.exists(self.f_name):
            with open(self.f_name, "r") as file:
                self.task = json.load(file)
        else:
            self.task = []
            
    def save_task(self):
        with open(self.f_name, "w") as file:
            json.dump(self.task, file, indent=4)

    def add_task(self):
        title = input("Write the Title: ")
        description = input("Write the Description: ")

        task = {
            "title": title,
            "description": description,
            "completed": False
        }

        self.task.append(task)
        self.save_task()
        print("Successfully Task Added")

    def view_task(self):
        if len(self.task) == 0:
            print("There is no task assigned")
        else:
            print("\nYour Task List")

            for i in range(len(self.task)):
                if self.task[i]["completed"] == True:
                    status = "Completed"
                else:
                    status = "Not Completed"

                print(str(i + 1) + ". " + "Title: "+ self.task[i]["title"] + ".  Description: " + self.task[i]["description"] + " [" + status + "]")

    def delete_task(self):
        if len(self.task) == 0:
            print("There is no task available for delete")
        else:
            self.view_task()
            taskNo = input("Enter Task Number to Delete: ")

            if taskNo.isdigit():
                number = int(taskNo)

                if number >= 1 and number <= len(self.task):
                    del self.task[number - 1]
                    self.save_task()
                    print("Successfully Task Deleted")
                else:
                    print("Task Number is not available")
            else:
                print("Please enter valid task number")

    def complete(self):
        if len(self.task) == 0:
            print("There is no task available to mark as completed")
        else:
            self.view_task()
            taskNo = input("Enter task number to mark as completed: ")

            if taskNo.isdigit():
                number = int(taskNo)

                if number >= 1 and number <= len(self.task):
                    self.task[number - 1]["completed"] = True
                    self.save_task()
                    print("Task marked as completed!")
                else:
                    print("Task Number is not available")
            else:
                print("Please enter valid task number")


tm = TaskManager()
tm.load_task()

while True:
    print("\n Task Tracker ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    c = input("Enter the Number You want to do: ")

    if c == "1":
        tm.add_task()

    elif c == "2":
        tm.view_task()

    elif c == "3":
        tm.delete_task()

    elif c == "4":
        tm.complete()

    elif c == "5":
        print("Exit The program")
        break

    else:
        print("Enter a number from 1 to 5")