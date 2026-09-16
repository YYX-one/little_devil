from PySide6.QtWidgets import QLabel, QDialog, QTextEdit
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QLabel,
    QDialog,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtWidgets import QPushButton
from llm import chat


class DialogueController:
    
    def __init__(self, devil):
        self.devil = devil
        self.chat_window = ChatWindow()

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

    def open_chat(self):
        self.chat_window.show()


class ChatWindow(QDialog):
    def __init__(self):
        super().__init__()
        

        self.setWindowTitle("Little Devil")
        self.resize(400, 500)
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)


        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText(
            "Type something..."
        )

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(
            self.send_message
        )

        self.input_box.returnPressed.connect(
            self.send_message
        )
        main_layout = QVBoxLayout()

        main_layout.addWidget(self.chat_history)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.input_box)
        bottom_layout.addWidget(self.send_button)

        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

    def send_message(self):
        message = self.input_box.text()

        if not message:
            return

        self.chat_history.append(
            f"You: {message}"
        )

        self.input_box.clear()

        reply = chat(message)

        self.chat_history.append(
            f"Peanut Butter: {reply}"
        )