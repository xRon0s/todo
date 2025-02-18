# main.py
import sys
from PySide6.QtWidgets import QApplication
from app import TodoApp
from PySide6.QtWidgets import QInputDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TodoApp()

    # アプリケーションが終了する前に保存
    app.aboutToQuit.connect(main_window.task_manager.save_data)

    main_window.show()
    sys.exit(app.exec())
