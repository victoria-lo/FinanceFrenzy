from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTimer

import pandas as pd
import sys

from stock_exchange import StockExchangeDialog


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Financial Times")
        self.setWindowIcon(QIcon("./assets/financial-times.png"))
        self.setFixedHeight(1080)
        self.setFixedWidth(1920)

        self.day = 0
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.a_day_has_passed)
        self.timer.start()
        self.create_widgets()

        self.consumer_dis_data = pd.read_csv("./data/SP-500-Consumer-Discretionary-Historical-Data.csv")
        self.consumer_stp_data = pd.read_csv("./data/SP-500-Consumer-Staples-Historical-Data.csv")
        self.energy_data = pd.read_csv("./data/SP-500-Energy-Historical-Data.csv")
        self.finance_data = pd.read_csv("./data/SP-500-Financials-Historical-Data.csv")
        self.healthcare_data = pd.read_csv("./data/SP-500-Health-Care-Historical-Data.csv")
        self.industrials_data = pd.read_csv("./data/SP-500-Industrials-Historical-Data.csv")
        self.it_data = pd.read_csv("./data/SP-500-Information-Technology-Historical-Data.csv")
        self.materials_data = pd.read_csv("./data/SP-500-Materials-Historical-Data.csv")
        self.real_estate_data = pd.read_csv("./data/SP-500-Real-Estate-Historical-Data.csv")
        self.telecom_data = pd.read_csv("./data/SP-500-Telecom-Services-Historical-Data.csv")
        self.utilities_data = pd.read_csv("./data/SP-500-Utilities-Historical-Data.csv")

        self.inflation_data = pd.read_csv("./data/Inflation.csv")
        self.interest_data = pd.read_csv("./data/Interest_rates.csv")

        self.stock_exchange_dlg = None

    def create_widgets(self):
        stock_exchange_btn = QPushButton("Stock Exchange", self)
        stock_exchange_btn.setGeometry(1650, 1000, 200, 50)
        stock_exchange_btn.setIcon(QIcon("./assets/stock-exchange.png"))
        stock_exchange_btn.setFont(QFont("Arial", 12))
        stock_exchange_btn.clicked.connect(self.open_stock_exchange)

    def open_stock_exchange(self):
        self.stock_exchange_dlg = StockExchangeDialog(self)
        self.stock_exchange_dlg.exec()

    def a_day_has_passed(self):
        self.day += 1
        print("A day has passed...")
        if self.stock_exchange_dlg is not None:
            self.stock_exchange_dlg.set_table_values()

        if self.day > 365 * 5 + 1:
            self.timer.stop()
            print("GAME OVER!")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())