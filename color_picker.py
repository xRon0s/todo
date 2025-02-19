# color_picker.py
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMouseEvent, QImage, QPixmap


class ColorPicker(QLabel):
    def __init__(self, parent=None, color_label=None, rgb_label=None, hex_label=None):
        super().__init__(parent)

        self.color_label = color_label
        self.rgb_label = rgb_label
        self.hex_label = hex_label

        self.setMouseTracking(True)
        self.image = None
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(400, 400)

    def setImage(self, image: QImage):
        self.image = image
        pixmap = QPixmap.fromImage(self.image)
        scaled_pixmap = pixmap.scaled(
            400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(scaled_pixmap)
        self.setFixedSize(scaled_pixmap.size())

    def mousePressEvent(self, event: QMouseEvent):
        if self.image and event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            if 0 <= x < self.width() and 0 <= y < self.height():
                scaled_x = x * self.image.width() / self.width()
                scaled_y = y * self.image.height() / self.height()

                pixel_color = self.image.pixelColor(
                    int(scaled_x), int(scaled_y))

                # カラーメッセージを直接表示
                hex_color = f"#{pixel_color.red():02x}{pixel_color.green():02x}{pixel_color.blue():02x}"
                self.color_label.setText(f"Selected Color: {hex_color}")
                self.rgb_label.setText(
                    f"RGB: ({pixel_color.red()}, {pixel_color.green()}, {pixel_color.blue()})")
                self.hex_label.setText(f"HEX: {hex_color}")
                self.setCursor(Qt.CrossCursor)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.image:
            x = event.pos().x()
            y = event.pos().y()
            if 0 <= x < self.width() and 0 <= y < self.height():
                scaled_x = x * self.image.width() / self.width()
                scaled_y = y * self.image.height() / self.height()

                pixel_color = self.image.pixelColor(
                    int(scaled_x), int(scaled_y))

                # カラーメッセージを直接表示
                hex_color = f"#{pixel_color.red():02x}{pixel_color.green():02x}{pixel_color.blue():02x}"
                self.color_label.setText(f"Selected Color: {hex_color}")
                self.rgb_label.setText(
                    f"RGB: ({pixel_color.red()}, {pixel_color.green()}, {pixel_color.blue()})")
                self.hex_label.setText(f"HEX: {hex_color}")
                self.setCursor(Qt.CrossCursor)
            else:
                self.setCursor(Qt.ArrowCursor)
