from PySide6.QtCore import (
    QObject,
    Signal,
    QTimer,
    QPropertyAnimation,
    QPoint,
    QEasingCurve
)


class MovementController(QObject):
    startup_finished = Signal()

    def __init__(self, devil):
        super().__init__()

        self.devil = devil
        # 闲置行为计时器
        self.idle_timer = QTimer(self)
        self.idle_timer.timeout.connect(
            self.random_idle_action
        )

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
        # 启动动作结束

        self.startup_finished.emit()
        self.idle_timer.start(5000)

    def random_idle_action(self):
        # 随机决定花生酱是否进行闲置行为

        import random

        # 10%的概率触发行为
        if random.random() < 0.1:
            self.spin_clockwise()

    def spin_clockwise(self):
        """顺时针旋转两圈"""

        self.spin_animation = QPropertyAnimation(
            self.devil,
            b"angle"
        )

        self.spin_animation.setDuration(2000)

        self.spin_animation.setStartValue(0)
        self.spin_animation.setEndValue(720)

        self.spin_animation.setEasingCurve(
            QEasingCurve.InOutQuad
        )

        self.spin_animation.finished.connect(
            self.pause_after_first_spin
        )

        self.spin_animation.start()

    def pause_after_first_spin(self):
        """第一次旋转结束后的停顿"""

        QTimer.singleShot(
            1000,
            self.spin_counterclockwise
        )

    def spin_counterclockwise(self):
        """快速逆时针旋转三圈"""

        self.spin_animation = QPropertyAnimation(
            self.devil,
            b"angle"
        )

        self.spin_animation.setDuration(900)

        self.spin_animation.setStartValue(720)
        self.spin_animation.setEndValue(-360)

        self.spin_animation.setEasingCurve(
            QEasingCurve.InOutQuad
        )

        self.spin_animation.finished.connect(
            self.spin_fast_clockwise
        )

        self.spin_animation.start()

    def spin_fast_clockwise(self):
        """高速顺时针旋转十圈"""

        self.spin_animation = QPropertyAnimation(
            self.devil,
            b"angle"
        )

        self.spin_animation.setDuration(1500)

        self.spin_animation.setStartValue(-360)
        self.spin_animation.setEndValue(3240)

        self.spin_animation.setEasingCurve(
            QEasingCurve.Linear
        )

        self.spin_animation.finished.connect(
            self.pause_before_jump
        )

        self.spin_animation.start()

    def pause_before_jump(self):
        """高速旋转结束后的停顿"""

        QTimer.singleShot(
            1000,
            self.jump_one
        )

    def jump_one(self):
        """第一次跳跃"""

        original_pos = self.devil.pos()

        self.jump_animation = QPropertyAnimation(
            self.devil,
            b"pos"
        )

        self.jump_animation.setDuration(300)

        self.jump_animation.setStartValue(
            original_pos
        )

        self.jump_animation.setKeyValueAt(
            0.5,
            original_pos + QPoint(0, -30)
        )

        self.jump_animation.setEndValue(
            original_pos
        )

        self.jump_animation.finished.connect(
            self.jump_two
        )

        self.jump_animation.start()

    def jump_two(self):
        """第二次跳跃"""

        original_pos = self.devil.pos()

        self.jump_animation = QPropertyAnimation(
            self.devil,
            b"pos"
        )

        self.jump_animation.setDuration(300)

        self.jump_animation.setStartValue(
            original_pos
        )

        self.jump_animation.setKeyValueAt(
            0.5,
            original_pos + QPoint(0, -30)
        )

        self.jump_animation.setEndValue(
            original_pos
        )

        # 原代码缺少这一句，导致第二次跳跃后动画链中断，现补上
        self.jump_animation.start()