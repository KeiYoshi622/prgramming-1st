import json, os

class Task:
    def __init__(self, title, priority='middle'):
        self.title = title
        self.priority = priority

    def __str__(self):
        return f"[{self.priority}] {self.title}"

    def to_dict(self):
        return {"title": self.title, "priority": self.priority}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["priority"])


class TodoList:
    def __init__(self):
        self.tasks = []
        self.dir_current = os.path.dirname(os.path.abspath(__file__))

    def add_task(self, title, priority='midldle'):
        self.tasks.append(Task(title, priority))

    def show_tasks(self):
        print("To-Doリスト:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def remove_task(self, index):
        try:
            self.tasks.pop(index - 1)
            print("タスクを削除しました。")
        except IndexError:
            print("無効な番号です。")

    def save_to_json(self, file_name):
        with open(f"{self.dir_current}/{file_name}", 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        print(f"タスクを {file_name} に保存しました。")

    def load_from_json(self, file_name):
        try:
            with open(f"{self.dir_current}/{file_name}", 'r') as file:
                self.tasks = [Task.from_dict(data) for data in json.load(file)]
            print(f"タスクを {file_name} から読み込みました。")
        except FileNotFoundError:
            print(f"{file_name} が見つかりませんでした。")

my_todo = TodoList()
my_todo.add_task("go to japanese school", "high")
# my_todo.add_task("play with Mike", "middle")
my_todo.show_tasks()

# # 使用例
# my_todo = TodoList()
# my_todo.load_from_json("tasks.json")
# my_todo.add_task("買い物", "高")
# my_todo.add_task("go to shop", "middle")
# my_todo.save_to_json("tasks.json")

# # 新しいインスタンスに読み込む
# new_todo = TodoList()
# new_todo.load_from_json("tasks.json")
# new_todo.show_tasks()
