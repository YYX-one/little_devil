from PySide6.QtCore import (
    QObject,
    QTimer,
    QPropertyAnimation,
    QPoint,
    QEasingCurve
)


class MovementController(QObject):
    def __init__(self, devil):
        super().__init__()

        self.devil = devil

        # 启动动作完成后，才进入后续行为
        self.startup_finished = False

    def start_startup_movement(self):
        """花生酱启动时的一套固定动作"""

        # 第一阶段：上下摇晃
        self.shake_up_down()
        QTimer.singleShot(
            250,
            self.shake_up_down
        )

    def shake_up_down(self):
        """轻微上下摇晃"""

        original_pos = self.devil.pos()

        self.shake_animation = QPropertyAnimation(
            self.devil,
            b"pos"
        )

        self.shake_animation.setDuration(400)

        self.shake_animation.setKeyValueAt(
            0,
            original_pos
        )

        self.shake_animation.setKeyValueAt(
            0.25,
            original_pos + QPoint(0, -5)
        )

        self.shake_animation.setKeyValueAt(
            0.5,
            original_pos + QPoint(0, 5)
        )

        self.shake_animation.setKeyValueAt(
            0.75,
            original_pos + QPoint(0, -3)
        )

        self.shake_animation.setKeyValueAt(
            1,
            original_pos
        )

        self.shake_animation.finished.connect(
            self.move_left
        )

        self.shake_animation.start()

    def move_left(self):
        """睡醒后笨拙地向左挪"""

        start_pos = self.devil.pos()
        end_pos = start_pos + QPoint(-25, 0)

        self.left_animation = QPropertyAnimation(
            self.devil,
            b"pos"
        )

        self.left_animation.setDuration(650)

        self.left_animation.setStartValue(start_pos)
        self.left_animation.setEndValue(end_pos)

        self.left_animation.setEasingCurve(
            QEasingCurve.InOutQuad
        )

        self.left_animation.finished.connect(
            self.move_right
        )

        self.left_animation.start()

    def move_right(self):
        """向右走，但走得比刚才远一点"""

        start_pos = self.devil.pos()
        end_pos = start_pos + QPoint(42, 0)

        self.right_animation = QPropertyAnimation(
            self.devil,
            b"pos"
        )

        self.right_animation.setDuration(850)

        self.right_animation.setStartValue(start_pos)
        self.right_animation.setEndValue(end_pos)

        self.right_animation.setEasingCurve(
            QEasingCurve.InOutQuad
        )

        self.right_animation.finished.connect(
            self.finish_startup_movement
        )

        self.right_animation.start()

    def finish_startup_movement(self):
        """启动动作结束"""

        self.startup_finished = True

        print("花生酱：Rise and shine, you tedious fool.")