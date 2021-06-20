from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFrame
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTimer

import pandas as pd
import sys

from stock_exchange import StockExchangeDialog
from assets import AssetsDialog
from liabilities import LiabilitiesDialog
from cashflows import CashflowsDialog


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Financial Times")
        self.setWindowIcon(QIcon("./assets/financial-times.png"))
        self.setFixedHeight(1080)
        self.setFixedWidth(1350)
        self.newsFrame = QFrame(self)
        self.newsFrame.setGeometry(100, 50, 1900, 900)
        self.newsFrame.setStyleSheet("QWidget { background-image: url(./assets/news_template.png); background-repeat: no-repeat }")

        self.day = 0
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.a_day_has_passed)
        self.timer.start()

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

        self.cashflows = []
        self.cash = 2000
        self.interest_rate = 0
        self.inflation_rate = 0

        self.date_lbl = QLabel("", self)
        self.date_lbl.setFont(QFont("Arial", 12))
        self.date_lbl.setGeometry(50, 30, 100, 20)
        self.set_date()

        self.cash_lbl = QLabel("", self)
        self.cash_lbl.setFont(QFont("Arial", 12))
        self.cash_lbl.setGeometry(50, 70, 200, 20)
        self.set_cash()

        self.interest_rate_lbl = QLabel("", self)
        self.interest_rate_lbl.setFont(QFont("Arial", 12))
        self.interest_rate_lbl.move(1150, 30)

        self.inflation_rate_lbl = QLabel("", self)
        self.inflation_rate_lbl.setFont(QFont("Arial", 12))
        self.inflation_rate_lbl.move(1150, 70)

        self.headline_lbl = QLabel("", self)
        self.headline_lbl.setFont(QFont("Times New Roman", 32))
        self.headline_lbl.setWordWrap(True)
        self.headline_lbl.setGeometry(300, 120, 780, 700)

        self.set_interest_rates()
        self.set_inflation_rates()
        self.stocks = []
        self.news = [
            {
                "headline": "First Business Day of Y2K Uneventful",
                "day": 3
            },
            {
                "headline": "BBC's reality tv show 'Castaways' begins recording",
                "day": 7
            },
            {
                "headline": "Flooding in Mozambique kills hundreds and displaces more than a million people",
                "day": 27
            },
            {
                "headline": "Bubble Bound to Burst When the Cash Fails to Materialize",
                "day": 62
            },
            {
                "headline": "Analysts Agree Market Has Only Witnessed Start of Internet fever; No End in Sight for Tech Craze",
                "day": 67
            },
            {
                "headline": "The Stock Market Bubble That Is Likely To Go On Floating",
                "day": 70
            },
            {
                "headline": "Celera Genomics and the publicly funded Human Genome Project announce completed draft versions of the human genetic code",
                "day": 78
            },
            {
                "headline": "Oil prices surges to more than $30 a barrel",
                "day": 171
            },
            {
                "headline": "Gaming taking off as Nintendo sold over 100 million Game Boy consoles",
                "day": 180
            },
            {
                "headline": "Bubble Bursts: Iron Laws of the Market Bring a Sharp Dose of Reality",
                "day": 240
            },
            {
                "headline": "Wikipedia launched by Jimmy Wales and Larry Sanger",
                "day": 261
            },
            {
                "headline": "Average age of a married man in the UK rises above 30 for the first time",
                "day": 265
            },
            {
                "headline": "Working draft of the human genome published",
                "day": 312
            },
            {
                "headline": "Dotcom bubble bursts as share prices tumble; companies such as boo.com and infospace go bankrupt",
                "day": 318
            },
            {
                "headline": "George Bush refuses to endorse the Kyoto protocol",
                "day": 320
            },
            {
                "headline": "Terrorist attacks on the World Trade Centre and the Pentagon kill nearly 3,000 people",
                "day": 430
            },
            {
                "headline": "Invasion of Afghanistan: the war on terror begins",
                "day": 450
            },
            {
                "headline": "New Home Buyers, Don't Fret!; Economy Slows, But Home Sales Are Hot",
                "day": 462
            },
            {
                "headline": "Enron goes bust at a cost of $17 billion",
                "day": 485
            },
            {
                "headline": "The Euro is introduced into 12 countries within the Euro-zone, including France and Germany",
                "day": 512
            },
            {
                "headline": "Scientists begin to create tiny strands of genetic material, RNA, that promise to revolutionise medicine",
                "day": 520
            },
            {
                "headline": "Fannie Mae Sees No End to Housing Boom",
                "day": 532
            },
            {
                "headline": "Weathering Recession, Housing Market Continues to Roar",
                "day": 542
            },
            {
                "headline": "WorldCom collapses after an investigation into fraud of $3.8 billion",
                "day": 621
            },
            {
                "headline": "Housing Market Surges to Record Levels",
                "day": 652
            },
            {
                "headline": "The Prestige oil tanker spills its 77,000-tonne cargo off the coast of Spain, causing the world's worst oil spill",
                "day": 710
            },
            {
                "headline": "The first cases of a new respiratory disease, SARS, emerge in Hong Kong, later spreading around the world",
                "day": 760
            },
            {
                "headline": "More People are Looking to Remortgage Their Property",
                "day": 860
            },
            {
                "headline": "Home Construction Soars to 17-Year High; October Figures Defy Predictions of Decline",
                "day": 1125
            },
            {
                "headline": "Facebook founded by Harvard university student Mark Zuckerberg. The site now has 300 million active users",
                "day": 1212
            },
            {
                "headline": "Median Home Price Up 9.1%",
                "day": 1380
            }

        ]
        self.create_widgets()

        self.stock_exchange_dlg = None
        self.cashflows_dlg = None
        self.asset_dlg = None
        self.liabilities_dlg = None

    def create_widgets(self):
        stock_exchange_btn = QPushButton("Stock Exchange", self)
        stock_exchange_btn.setGeometry(1040, 1000, 200, 50)
        stock_exchange_btn.setIcon(QIcon("./assets/stock-exchange.png"))
        stock_exchange_btn.setFont(QFont("Arial", 12))
        stock_exchange_btn.clicked.connect(self.open_stock_exchange)

        stock_exchange_btn = QPushButton("Cashflows", self)
        stock_exchange_btn.setGeometry(720, 1000, 200, 50)
        stock_exchange_btn.setIcon(QIcon("./assets/money.png"))
        stock_exchange_btn.setFont(QFont("Arial", 12))
        stock_exchange_btn.clicked.connect(self.open_cashflows)

        asset_btn = QPushButton("Assets", self)
        asset_btn.setGeometry(100, 1000, 200, 50)
        asset_btn.setFont(QFont("Arial", 12))
        asset_btn.setIcon(QIcon("./assets/assets.png"))
        asset_btn.clicked.connect(self.open_asset)

        liabilities_btn = QPushButton("Liabilities", self)
        liabilities_btn.setGeometry(420, 1000, 200, 50)
        liabilities_btn.setFont(QFont("Arial", 12))
        liabilities_btn.setIcon(QIcon("./assets/liabilities.png"))
        liabilities_btn.clicked.connect(self.open_liabilities)

    def open_stock_exchange(self):
        self.stock_exchange_dlg = StockExchangeDialog(self)
        self.stock_exchange_dlg.exec()

    def open_cashflows(self):
        self.cashflows_dlg = CashflowsDialog(self)
        self.cashflows_dlg.exec()

    def open_asset(self):
        self.asset_dlg = AssetsDialog(self)
        self.asset_dlg.exec()

    def open_liabilities(self):
        self.liabilities_dlg = LiabilitiesDialog(self)
        self.liabilities_dlg.exec()

    def set_interest_rates(self):
        self.interest_rate = self.interest_data.iat[self.day // 20, 1]
        self.interest_rate_lbl.setText("Interest Rate: " + str(self.interest_rate) + "%")
        self.repaint()

    def set_inflation_rates(self):
        self.inflation_rate = self.inflation_data.iat[self.day // 365, 1]
        self.inflation_rate_lbl.setText("Inflation Rate: " + str(self.inflation_rate.__round__(2)) + "%")
        self.repaint()

    def buy_stock(self, stock):
        k = len(self.energy_data.columns) - self.day
        self.cash -= stock['price']
        self.set_cash()
        self.cashflows.append({
            "value": -stock["price"],
            "date": self.energy_data.iloc[k]["Date"]
        })
        self.stocks.append(stock)

    def sell_stock(self, assets_window):
        k = len(self.energy_data.columns) - self.day
        total = 0
        for stock in self.stocks:
            total += stock['price']
        self.cash += total
        self.set_cash()
        self.cashflows.append({
            "value": total,
            "date": self.energy_data.iloc[k]["Date"]
        })
        self.stocks = []
        assets_window.retranslateUi()

    def set_date(self):
        k = len(self.energy_data.columns) - self.day
        self.date_lbl.setText(self.energy_data.iloc[k]["Date"])
        self.repaint()

    def set_cash(self):
        self.cash_lbl.setText("Cash: $" + str(self.cash.__round__(2)))
        self.repaint()

    def display_news(self):
        news = next((item for item in self.news if item["day"] == self.day), None)
        if news:
            self.headline_lbl.setText(news["headline"])
            self.repaint()

    def a_day_has_passed(self):
        self.day += 1
        self.display_news()
        self.set_date()
        if self.stock_exchange_dlg is not None:
            self.stock_exchange_dlg.set_table_values()

        if self.day % 20 == 0:  # a month has passed (5 weekdays * 4 weeks) since we're not counting weekends
            print("A month has passed...")
            self.cash += 10000
            self.set_cash()
            self.set_interest_rates()
            k = len(self.energy_data.columns) - self.day
            self.cashflows.append({
                "value": 10000,
                "date": self.energy_data.iloc[k]["Date"]
            })
            if self.cashflows_dlg is not None:
                self.cashflows_dlg.set_table_values()

        if self.day % (52 * 5) == 0:
            print("A year has passed...")
            self.set_interest_rates()

        if self.day > (52 * 5) * 5 + 1:
            self.timer.stop()
            print("GAME OVER!")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
