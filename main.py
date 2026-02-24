import random
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QPen, QBrush
from PyQt6.QtCore import Qt, QRect


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окружность в PyQt6")
        self.resize(500, 500)
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.start)
        self.rads = [random.randint(50, 100) for _ in range(4)]
        self.started = False

    def start(self):
        self.started = True
        self.rads = [random.randint(50, 100) for _ in range(4)]
        self.update()

    def paintEvent(self, event):
        if self.started:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            pen = QPen(Qt.GlobalColor.black, 3)
            painter.setPen(pen)
            brush = QBrush(Qt.GlobalColor.yellow)
            painter.setBrush(brush)
            painter.drawEllipse(150 - self.rads[0], 150 - self.rads[0], self.rads[0], self.rads[0])
            painter.drawEllipse(150 - self.rads[1], 550 - self.rads[1], self.rads[1], self.rads[1])
            painter.drawEllipse(550 - self.rads[2], 150 - self.rads[2], self.rads[2], self.rads[2])
            painter.drawEllipse(550 - self.rads[3], 550 - self.rads[3], self.rads[3], self.rads[3])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())
