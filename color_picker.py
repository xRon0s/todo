#colo_picker.py
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt ,QPoint
from PySide6.QtGui import QMouseEvent, QImage, QPixmap


class ColorPicker(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.image = None
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(400, 400)

    def setImage(self, image: QImage):
        self.image = QImage(image)
        pixmap = QPixmap.fromImage(self.image)
        self.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))
        self.setFixedSize(pixmap.size())

    def mousePressEvent(self, event: QMouseEvent):
        if self.image and event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            if 0 <= x < self.image.width() and 0 <= y < self.image.height():
                pixel_color = self.image.pixelColor(x, y)
                Parent = self.parent()
                Parent.color_label.setText(f"Selected Color:  # {pixel_color.red():02x}{pixel_color.green():02x}{pixel_color.blue():02x}")
                Parent.rgb_label.setText(
                f"RGB: ({pixel_color.red()}, {pixel_color.green()}, {pixel_color.blue()})")
                Parent.hex_label.setText(
                f"HEX: #{pixel_color.red():02x}{pixel_color.green():02x}{pixel_color.blue():02x}")


    def mouseMoveEvent(self, event: QMouseEvent):
        if self.image and event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            if 0 <= x < self.image.width() and 0 <= y < self.image.height():
                pixel_color = self.image.pixelColor(x, y)
                parent = self.parent()
                hex_color = f'#{pixel_color.red():02x}{pixel_color.green():02x}{pixel_color.blue():02x}'
                parent.color_label.setText(f"Selected Color: {hex_color}")
                parent.rgb_label.setText(
                    f"RGB: ({pixel_color.red()}, {pixel_color.green()}, {pixel_color.blue()})")
                parent.hex_label.setText(f"HEX: {hex_color}")
                self.setCursor(Qt.CrossCursor)
            else:
                self.setCursor(Qt.ArrowCursor)
