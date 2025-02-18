# todo_app.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit
from tasks import TaskManager


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToDo App")
        self.setGeometry(300, 300, 300, 300)

        self.task_manager = TaskManager()
        self.layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("新しいタスクを入力...")
        self.layout.addWidget(self.task_input)

        self.add_button = QPushButton("追加", self)
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.list_widget = QListWidget(self)
        self.layout.addWidget(self.list_widget)

        self.delete_button = QPushButton("削除", self)
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            self.task_manager.add_task(task_text)
            self.update_task_list()
            self.task_input.clear()

    def delete_task(self):
        list_items = self.list_widget.selectedItems()
        if not list_items:
            return
        for item in list_items:
            index = self.list_widget.row(item)
            self.task_manager.delete_task(index)
            self.update_task_list()
            break  # 一度に一つのタスクだけ削除します

    def update_task_list(self):
        self.list_widget.clear()
        for task in self.task_manager.get_tasks():
            self.list_widget.addItem(task)
