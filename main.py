import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QFileDialog, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt
from color_picker import ColorPicker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Checker")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # レイアウトを縦に配置
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # 上部にボタンを配置
        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_button)

        # 画像を表示するラベルのためのレイアウト
        self.image_layout = QHBoxLayout()
        self.layout.addLayout(self.image_layout)

        # 画像を中央に配置
        self.color_picker = ColorPicker(self)
        self.image_layout.addWidget(self.color_picker)
        self.image_layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # その他の情報を表示するラベル
        self.color_label = QLabel("Selected Color: ")
        self.layout.addWidget(self.color_label)

        self.rgb_label = QLabel("RGB: ")
        self.layout.addWidget(self.rgb_label)

        self.hex_label = QLabel("HEX: ")
        self.layout.addWidget(self.hex_label)

        self.compare_label = QLabel("Compare Colors:")
        self.layout.addWidget(self.compare_label)

        self.color_inputs = []
        for i in range(4):
            color_input = QLineEdit()
            color_input.setPlaceholderText("Enter color code (HEX)")
            self.layout.addWidget(color_input)
            self.color_inputs.append(color_input)

        self.compare_button = QPushButton("Compare Colors")
        self.compare_button.clicked.connect(self.compare_colors)
        self.layout.addWidget(self.compare_button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

    def load_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if file_name:
            self.image = QImage(file_name)
            self.color_picker.setImage(self.image)

    def compare_colors(self):
        main_color_hex = self.hex_label.text().split(": ")[1]
        results = []
        main_color_hex = main_color_hex.lower()
        for input_field in self.color_inputs:
            compare_color_hex = input_field.text()
            if compare_color_hex:
                result = "Match" if main_color_hex.lower(
                ) == compare_color_hex.lower() else "No Match"
                results.append(f"{compare_color_hex}: {result}")

        self.result_label.setText("\n".join(results))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
