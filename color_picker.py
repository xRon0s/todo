from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMouseEvent, QImage, QPixmap


class ColorPicker(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)  # マウスの追跡を有効にする
        self.image = None
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(400, 400)  # 固定のサイズ

        # 画像の位置 (ウィンドウ内で画像の位置を取得)
        self.image_pos = QPoint(50, 50)  # 初期位置 (これを動的に計算しても良い)

    def setImage(self, image: QImage):
        self.image = image
        pixmap = QPixmap.fromImage(self.image)

        # 画像を400x400にリサイズ
        scaled_pixmap = pixmap.scaled(
            400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # リサイズ後の画像を設定
        self.setPixmap(scaled_pixmap)

        # 画像サイズに合わせてウィジェットのサイズを設定
        self.setFixedSize(scaled_pixmap.size())
        print("Image loaded successfully.")  # 画像が正常に読み込まれたか確認

    def mousePressEvent(self, event: QMouseEvent):
        if self.image and event.button() == Qt.LeftButton:
            # マウスの位置を画像内の位置に変換
            x = event.pos().x() - self.image_pos.x()
            y = event.pos().y() - self.image_pos.y()
            if 0 <= x < self.image.width() and 0 <= y < self.image.height():
                pixel_color = self.image.pixelColor(x, y)
                # ピクセルの色を表示
                print(f"Color picked at ({x}, {y}): {pixel_color.name()}")

                # 親ウィンドウの参照を取得
                from main import MainWindow
                parent = self.parent()
                if isinstance(parent, MainWindow):
                    hex_color = f"#{pixel_color.red():02x}{pixel_color.green():02x}{pixel_color.blue():02x}"
                    parent.color_label.setText(f"Selected Color: {hex_color}")
                    parent.rgb_label.setText(
                        f"RGB: ({pixel_color.red()}, {pixel_color.green()}, {pixel_color.blue()})")
                    parent.hex_label.setText(f"HEX: {hex_color}")

                    # カーソルをクロスに変更
                    self.setCursor(Qt.CrossCursor)
                else:
                    print("Parent is not MainWindow.")  # 親ウィンドウが取得できない場合
            else:
                print("Mouse click outside image.")  # 画像外でクリック

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.image:
            # マウスの位置を画像内の位置に変換
            x = event.pos().x() - self.image_pos.x()
            y = event.pos().y() - self.image_pos.y()
            if 0 <= x < self.image.width() and 0 <= y < self.image.height():
                pixel_color = self.image.pixelColor(x, y)
                # ピクセルの色を表示
                print(f"Mouse moved to ({x}, {y}): {pixel_color.name()}")

                # 親ウィンドウの参照を取得
                parent = self.parent()
                from main import MainWindow
                if isinstance(parent, MainWindow):
                    hex_color = f"#{pixel_color.red():02x}{pixel_color.green():02x}{pixel_color.blue():02x}"
                    parent.color_label.setText(f"Selected Color: {hex_color}")
                    parent.rgb_label.setText(
                        f"RGB: ({pixel_color.red()}, {pixel_color.green()}, {pixel_color.blue()})")
                    parent.hex_label.setText(f"HEX: {hex_color}")
                    parent.color_label.repaint()
                    parent.rgb_label.repaint()
                    parent.hex_label.repaint()
                    

                    # カーソルをクロスに変更
                    self.setCursor(Qt.CrossCursor)
                else:
                    print("Parent is not MainWindow.")  # 親ウィンドウが取得できない場合
            else:
                # 画像外でポインタを通常の矢印に変更
                self.setCursor(Qt.ArrowCursor)
