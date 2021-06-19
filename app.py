from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtGui import QIcon
import pandas as pd

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Financial Times")
        self.setWindowIcon(QIcon("./assets/financial-times.png"))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())