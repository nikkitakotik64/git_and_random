import random
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import Qt, QRect
from ui import Graphics


class CircleDrawer(Graphics):
    def __init__(self):
        super().__init__()
        self.rads = [random.randint(50, 100) for _ in range(4)]
        self.cols = [QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                     for _ in range(4)]
        self.started = False
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.started = True
        self.rads = [random.randint(50, 100) for _ in range(4)]
        self.cols = [QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                     for _ in range(4)]
        self.update()

    def paintEvent(self, event):
        if self.started:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            pen = QPen(Qt.GlobalColor.black, 3)
            painter.setPen(pen)
            brush = QBrush(self.cols[0])
            painter.setBrush(brush)
            painter.drawEllipse(150 - self.rads[0], 150 - self.rads[0], self.rads[0], self.rads[0])
            brush = QBrush(self.cols[1])
            painter.setBrush(brush)
            painter.drawEllipse(150 - self.rads[1], 550 - self.rads[1], self.rads[1], self.rads[1])
            brush = QBrush(self.cols[2])
            painter.setBrush(brush)
            painter.drawEllipse(550 - self.rads[2], 150 - self.rads[2], self.rads[2], self.rads[2])
            brush = QBrush(self.cols[3])
            painter.setBrush(brush)
            painter.drawEllipse(550 - self.rads[3], 550 - self.rads[3], self.rads[3], self.rads[3])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())
