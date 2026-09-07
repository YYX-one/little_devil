from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap
import sys
from pathlib import Path

from movement import MovementController

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = BASE_DIR / "assets" / "mini_devil.png"


class LittleDevil(QLabel):
    def __init__(self):
        super().__init__()

        # 窗口设置
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        # 加载恶魔图片
        pixmap = QPixmap(str(IMAGE_PATH))

        pixmap = pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.setPixmap(pixmap)

        # 鼠标拖动
        self.drag_offset = QPoint()

        # 创建移动控制器
        self.movement = MovementController(self)

    # 鼠标按下
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_offset = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )

    # 鼠标移动
    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(
                event.globalPosition().toPoint()
                - self.drag_offset
            )

    # 鼠标双击关闭
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.close()


app = QApplication(sys.argv)

devil = LittleDevil()
devil.show()

# 启动花生酱的固定动作
devil.movement.start_startup_movement()

sys.exit(app.exec())