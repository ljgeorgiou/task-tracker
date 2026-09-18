import json
from pathlib import Path
from typing import Any

class TaskList:
    def __init__(self) -> None:
        self.dictionary: dict[str, list[str]] = {}
        if Path("to_do_list.json").exists():
            with open("to_do_list.json") as f:
                self.dictionary = json.load(f)
        else:
            with open("to_do_list.json", "w") as f:
                json.dump(self.dictionary, f)

    def addTask(self, task: str) -> None:
        self.dictionary[task] = []
        with open("to_do_list.json", "w") as f:
            json.dump(self.dictionary, f)

    def deleteTask(self, task: str) -> None:
        try:
            del self.dictionary[task]
            with open("to_do_list.json", "w") as f:
                json.dump(self.dictionary, f)
        except KeyError:
            print(f"Task {task} does not exist in the to-do list.")
        
    def show(self) -> None:
        for key in self.dictionary:
            print(f"{self.dictionary[key]} : {key}")

    def completeTask(self, task: str) -> None:
        if task in self.dictionary:
            self.dictionary[task] = ["X"]
            with open("to_do_list.json", "w") as f:
                json.dump(self.dictionary, f)
        else:
            print(f"{task} does not exist in the list")

taskList = TaskList()

def to_int(answer: Any) -> int:
    try:
        return int(answer)
    except ValueError:
        print("Not an int\n\n")
        return -1

def is_valid_option(option: int) -> bool:
    return 1 <= option <= 5

task_list = TaskList()

while True:
    option_str = input(
        "To see your current list, type 1\n"
        "To add a task to your list, type 2\n"
        "To delete a task from your list, type 3\n"
        "To mark a task as completed, type 4\n"
        "To quit, type 5\n"
        "Type answer here: "
    )

    option_int = to_int(option_str)

    if not is_valid_option(option_int):
        continue

    if option_int == 1:
        print()
        task_list.show()
        print()

    elif option_int == 2:
        print()
        task: str = input("What task would you like to add: ")
        print()
        task_list.addTask(task)
        print()
        task_list.show()
        print()

    elif option_int == 3:
        print()
        task: str = input("What task would you like to delete: ")
        print()
        task_list.deleteTask(task)
        print()
        task_list.show()
        print()

    elif option_int == 4:
        print()
        task: str = input("What task would you like to complete: ")
        print()
        task_list.completeTask(task)
        print()
        task_list.show()
        print()

    elif option_int == 5:
        break