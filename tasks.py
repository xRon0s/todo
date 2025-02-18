import json


class Task:
    def __init__(self, name):
        self.name = name


class Folder:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]


class TaskManager:
    def __init__(self):
        self.folders = []
        self.load_data()

    def add_folder(self, folder_name):
        folder = Folder(folder_name)
        self.folders.append(folder)

    def get_folders(self):
        return self.folders  # 追加: フォルダーのリストを返すメソッド

    def load_data(self):
        try:
            with open('data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for folder_data in data['folders']:
                    folder = Folder(folder_data['name'])
                    for task_name in folder_data['tasks']:
                        folder.add_task(Task(task_name))
                    self.folders.append(folder)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('data.json', 'w', encoding='utf-8') as f:
            data = {
                'folders': []
            }
            for folder in self.folders:
                folder_data = {
                    'name': folder.name,
                    'tasks': [task.name for task in folder.tasks]
                }
                data['folders'].append(folder_data)
            json.dump(data, f, ensure_ascii=False, indent=4)
