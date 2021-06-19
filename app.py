from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Financial Times")
        self.setWindowIcon(QIcon("./assets/financial-times.png"))

        self.day = 0
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.a_day_has_passed)
        self.timer.start()

    def a_day_has_passed(self):
        self.day += 1
        print("A day has passed...")
        if self.day > 365 * 5 + 1:
            self.timer.stop()
            print("GAME OVER!")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())