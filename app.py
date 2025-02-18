# todo_app.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QTreeWidget, QTreeWidgetItem, QMessageBox, QInputDialog
from tasks import TaskManager, Task, Folder


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToDo App")
        self.setGeometry(300, 300, 400, 300)

        self.task_manager = TaskManager()
        self.layout = QVBoxLayout()

        self.folder_input = QLineEdit(self)
        self.folder_input.setPlaceholderText("新しいフォルダ名を入力...")
        self.layout.addWidget(self.folder_input)

        self.add_folder_button = QPushButton("フォルダ追加", self)
        self.add_folder_button.clicked.connect(self.add_folder)
        self.layout.addWidget(self.add_folder_button)

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("新しいタスク名を入力...")
        self.layout.addWidget(self.task_input)

        self.add_task_button = QPushButton("タスク追加", self)
        self.add_task_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_task_button)

        self.delete_button = QPushButton("選択したタスクを削除", self)
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)

        self.delete_folder_button = QPushButton("選択したフォルダを削除", self)
        self.delete_folder_button.clicked.connect(self.delete_folder)
        self.layout.addWidget(self.delete_folder_button)

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(["フォルダ", "タスク"])
        self.tree_widget.setDragEnabled(True)
        self.tree_widget.setDropIndicatorShown(True)
        self.tree_widget.setAcceptDrops(True)
        self.tree_widget.itemChanged.connect(self.folder_changed)
        self.tree_widget.itemDoubleClicked.connect(self.edit_folder_name)
        self.layout.addWidget(self.tree_widget)

        self.layout.setStretch(0, 0)
        self.setLayout(self.layout)

    def add_folder(self):
        folder_name = self.folder_input.text()
        if folder_name:
            self.task_manager.add_folder(folder_name)
            self.update_tree_widget()

    def add_task(self):
        task_name = self.task_input.text()
        if task_name:
            selected_items = self.tree_widget.selectedItems()
            if selected_items:
                selected_item = selected_items[0]
                if selected_item.parent() is None:
                    folder_index = self.tree_widget.indexOfTopLevelItem(
                        selected_item)
                    task = Task(task_name)
                    self.task_manager.folders[folder_index].add_task(task)
                    self.update_tree_widget()
                else:
                    # フォルダが選択されていない場合はメッセージボックスを表示
                    QMessageBox.warning(self, "エラー", "フォルダを選択してください")
            else:
                # フォルダが選択されていない場合はメッセージボックスを表示
                QMessageBox.warning(self, "エラー", "フォルダを選択してください")

    def delete_task(self):
        selected_items = self.tree_widget.selectedItems()
        for selected_item in selected_items:
            if selected_item.parent() is not None:
                parent_folder_index = self.tree_widget.indexOfTopLevelItem(
                    selected_item.parent())
                self.task_manager.folders[parent_folder_index].delete_task(
                    selected_item.parent().indexOfChild(selected_item))
        self.update_tree_widget()

    def delete_folder(self):
        selected_items = self.tree_widget.selectedItems()
        for selected_item in selected_items:
            if selected_item.parent() is None:
                folder_index = self.tree_widget.indexOfTopLevelItem(
                    selected_item)
                del self.task_manager.folders[folder_index]
        self.update_tree_widget()


    def update_tree_widget(self):
        self.tree_widget.clear()
        for folder in self.task_manager.folders:
            folder_item = QTreeWidgetItem([folder.name])
            for task in folder.tasks:
                task_item = QTreeWidgetItem([task.name])
                folder_item.addChild(task_item)
            self.tree_widget.addTopLevelItem(folder_item)


    def folder_changed(self, item, column):
        if column == 0:
            if item.parent() is None:
                folder_index = self.tree_widget.indexOfTopLevelItem(item)
                self.task_manager.folders[folder_index].name = item.text(column)
            else:
                folder_index = self.tree_widget.indexOfTopLevelItem(
                    item.parent())
                task_index = item.parent().indexOfChild(item)
                self.task_manager.folders[folder_index].tasks[
                    task_index].name = item.text(column)

    def edit_folder_name(self, item):
        if item.parent() is None:
            folder_index = self.tree_widget.indexOfTopLevelItem(item)
            new_folder_name, ok = QInputDialog.getText(
                self, "フォルダ名の編集", "新しいフォルダ名", text=item.text(0))
            if ok:
                self.task_manager.folders[folder_index].name = new_folder_name
                item.setText(0, new_folder_name)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()
            

    def dropEvent(self, event):
        if event.mimeData().hasText():
            target_item = self.tree_widget.itemAt(event.pos())
            if target_item and target_item.parent():
                task_name = event.mimeData().text()
                parent_folder = target_item.parent()
                # フォルダのインデックスを取得
                folder_index = self.tree_widget.indexOfTopLevelItem(
                    parent_folder)

                # 新しいタスクを追加する
                task = Task(task_name)
                self.task_manager.folders[folder_index].add_task(task)

                # フォルダの中のタスクリストを更新
                self.update_tree_widget()

                # 移動されたタスクを元のタスクリストから削除
                selected_items = self.tree_widget.selectedItems()
                for selected_item in selected_items:
                    if selected_item.parent() is not None:  # タスクであれば削除
                        parent_folder_index = self.tree_widget.indexOfTopLevelItem(
                            selected_item.parent())
                        self.task_manager.folders[parent_folder_index].delete_task(
                            selected_item.parent().indexOfChild(selected_item))
                        break

            event.accept()
        else:
            event.ignore()

    def closeEvent(self, event):
        self.task_manager.save_data()  # アプリケーションの終了時にデータを保存
        event.accept()  # 終了処理の受け入れ
