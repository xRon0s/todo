import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QFileDialog, QHBoxLayout, QSpacerItem, QSizePolicy, QFrame
from PySide6.QtGui import QImage, QColor
from color_picker import ColorPicker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Checker")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

      
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        
        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_button)

        
        self.color_label = QLabel("Selected Color: ")
        self.layout.addWidget(self.color_label)

        self.rgb_label = QLabel("RGB: ")
        self.layout.addWidget(self.rgb_label)

        self.hex_label = QLabel("HEX: ")
        self.layout.addWidget(self.hex_label)

        self.image_layout = QHBoxLayout()
        self.color_picker = ColorPicker(
            self, self.color_label, self.rgb_label, self.hex_label)
        self.image_layout.addWidget(self.color_picker)
        self.image_layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.layout.addLayout(self.image_layout)

        self.input_color_label = QLabel("Entered Colors:")
        self.layout.addWidget(self.input_color_label)

    
        self.color_inputs = []
        for i in range(4):
            color_input = QLineEdit()
            color_input.setPlaceholderText("Enter color code (HEX)")
            color_input.textChanged.connect(self.update_color_display)
            self.layout.addWidget(color_input)
            self.color_inputs.append(color_input)

        self.compare_button = QPushButton("Compare Colors")
        self.compare_button.clicked.connect(self.compare_colors)
        self.layout.addWidget(self.compare_button)

      
        self.color_displays = []
        self.color_display_layout = QHBoxLayout()  
        self.color_display_layout.setSpacing(5)  

        for i in range(4):
            
            color_display = QFrame()
            color_display.setFixedSize(160, 160) 
            color_display.setStyleSheet("background-color: #FFFFFF;")
            self.color_display_layout.addWidget(color_display)
            self.color_displays.append(color_display)

       
        self.layout.addLayout(self.color_display_layout)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

    def load_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if file_name:
            self.image = QImage(file_name)
            self.color_picker.setImage(self.image)

    def update_color_display(self):
        """入力された色コードに基づいて色表示を更新"""
        for i, input_field in enumerate(self.color_inputs):
            color_code = input_field.text().strip()
            if self.is_valid_hex(color_code):
                self.color_displays[i].setStyleSheet(
                    f"background-color: {color_code};")
            else:
                self.color_displays[i].setStyleSheet(
                    "background-color: #FFFFFF;")

    def is_valid_hex(self, hex_code):
        """入力された色コードが有効なHEXコードか確認"""
        if len(hex_code) == 7 and hex_code[0] == "#":
            try:
                int(hex_code[1:], 16)
                return True
            except ValueError:
                return False
        return False

    def compare_colors(self):
        main_color_hex = self.hex_label.text().split(
            ": ")[1].replace("#", "").lower()
        results = []
        for input_field in self.color_inputs:
            compare_color_hex = input_field.text().replace("#", "").lower()
            if compare_color_hex:
                result = "Match" if main_color_hex == compare_color_hex else ""
                if result:  
                    results.append(f"{input_field.text()}: {result}")

        
        self.result_label.setText("\n".join(results))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
