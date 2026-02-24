from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class Graphics(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окружность в PyQt6")
        self.resize(600, 600)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(250, 250, 100, 100)
