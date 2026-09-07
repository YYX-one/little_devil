from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QTimer


class DialogueController:
    def __init__(self, devil):
        self.devil = devil

        # 创建对话框
        self.dialogue = QLabel(
            "Rise and shine, you tedious fool."
        )

        # 对话框基本设置
        self.dialogue.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.dialogue.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px solid black;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        self.dialogue.adjustSize()

    def show_dialogue(self):
        """显示花生酱的对话"""

        # 获取花生酱当前的位置
        devil_pos = self.devil.pos()

        # 把对话框放在花生酱的右上方
        dialogue_x = devil_pos.x() + self.devil.width()
        dialogue_y = devil_pos.y()

        self.dialogue.move(
            dialogue_x,
            dialogue_y
        )

        self.dialogue.show()

        QTimer.singleShot(
            3000,
            self.dialogue.hide
        )