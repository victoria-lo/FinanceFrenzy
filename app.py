from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon

import pandas as pd
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
        healthcare_data = pd.read_csv("./data/SP-500-Health-Care-Historical-Data.csv")
        finance_data = pd.read_csv("./data/SP-500-Financials-Historical-Data.csv")
        energy_data = pd.read_csv("./data/SP-500-Energy-Historical-Data.csv")
        it_data = pd.read_csv("./data/SP-500-Information-Technology-Historical-Data.csv")
        industrials_data = pd.read_csv("./data/SP-500-Industrials-Historical-Data.csv")
        consumer_dis_data = pd.read_csv("./data/SP-500-Consumer-Discretionary-Historical-Data.csv")
        consumer_stp_data = pd.read_csv("./data/SP-500-Consumer-Staples-Historical-Data.csv")
        real_estate_data = pd.read_csv("./data/SP-500-Real-Estate-Historical-Data.csv")
        telecom_data = pd.read_csv("./data/SP-500-Telecom-Services-Historical-Data.csv")
        utilities_data = pd.read_csv("./data/SP-500-Utilities-Historical-Data.csv")
        materials_data = pd.read_csv("./data/SP-500-Materials-Historical-Data.csv")
        inflation_data = pd.read_csv("./data/Inflation.csv")
        interest_data = pd.read_csv("./data/Interest_rates.csv")

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