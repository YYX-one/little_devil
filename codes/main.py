from PySide6.QtWidgets import QApplication, QLabel, QMenu
from PySide6.QtCore import Qt, QPoint, Property
from PySide6.QtGui import QPixmap, QPainter
import sys
from pathlib import Path

from movement import MovementController
from dialogue import DialogueController

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = BASE_DIR / "assets" / "mini_devil.png"


class LittleDevil(QLabel):
    def __init__(self):
        super().__init__()
        self._angle = 0

        # 窗口设置
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        # 加载恶魔图片
        self.original_pixmap = QPixmap(str(IMAGE_PATH))

        self.original_pixmap = self.original_pixmap.scaled(
            200,
            200,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.setPixmap(self.original_pixmap)

        # 鼠标拖动
        self.drag_offset = QPoint()

        # 创建移动控制器
        self.movement = MovementController(self)
        # 创建对话控制器
        self.dialogue = DialogueController(self)
        self.movement.startup_finished.connect(
            self.dialogue.show_dialogue
        )

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


    def contextMenuEvent(self, event):
        menu = QMenu(self)

        talk_action = menu.addAction("Talk")

        action = menu.exec(event.globalPos())

        if action == talk_action:
            self.dialogue.open_chat()

    

    def get_angle(self):
        return self._angle

    def set_angle(self, angle):
        self._angle = angle
        self.update()

    angle = Property(float, get_angle, set_angle)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.SmoothPixmapTransform
        )

    # 整张 pixmap 的中心
        pixmap_center_x = self.original_pixmap.width() / 2
        pixmap_center_y = self.original_pixmap.height() / 2

    # 花生酱本体的中心
        pivot_x = 84
        pivot_y = 55

        painter.translate(
            pivot_x,
            pivot_y
        )

        painter.rotate(self.angle)

        painter.translate(
            -pivot_x,
            -pivot_y
        )

        painter.drawPixmap(
            0,
            0,
            self.original_pixmap
        )


app = QApplication(sys.argv)

devil = LittleDevil()
devil.show()

# 启动花生酱的固定动作
devil.movement.start_startup_movement()

sys.exit(app.exec())