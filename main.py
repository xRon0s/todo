# main.py
import sys
from PySide6.QtWidgets import QApplication
from app import TodoApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TodoApp()
    main_window.show()
    sys.exit(app.exec_())
