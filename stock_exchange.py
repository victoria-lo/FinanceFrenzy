from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtGui import QBrush, QColor, QIcon
from PyQt6.QtCore import QSize

from functools import partial


class StockExchangeDialog(QDialog):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.setWindowTitle("Stock Exchange")
        self.setMinimumSize(QSize(900, 360))
        self.setWindowIcon(QIcon("./assets/stock-exchange.png"))

        self.table = QTableWidget(self)
        self.headers = ["Symbol", "Name", "Price", "Open", "High", "Low", "Vol.", "Change %"]
        self.table.setColumnCount(len(self.headers))
        self.table.setRowCount(11)
        # Set the table headers
        self.table.setHorizontalHeaderLabels(self.headers)

        # Set the table values
        self.set_table_values()

        # Resize of the rows and columns based on the content
        self.table.setFixedWidth(824)
        self.table.setFixedHeight(360)
        self.table.show()

        # Set Buy buttons
        k = len(self.app.it_data.columns) - self.app.day
        stocks = [
            {
                "symbol": "SP500.25",
                "name": "Consumer Discretionary",
                "price": self.app.consumer_dis_data.iloc[k]["Price"]
            },
            {
                "symbol": "SP500.30",
                "name": "Consumer Staples",
                "price": self.app.consumer_stp_data.iloc[k]["Price"]
            },
            {
                "symbol": "SP500.10",
                "name": "Energy",
                "price": self.app.energy_data.iloc[k]["Price"]
            },
            {
                "symbol": "SP500.40",
                "name": "Financials",
                "price": self.app.finance_data.iloc[k]["Price"]
            },
            {
                "symbol": "SP500.35",
                "name": "Healthcare",
                "price": self.app.healthcare_data.iloc[k]["Price"]
            },
            {
                "symbol": "SP500.20",
                "name": "Industrials",
                "price": self.app.industrials_data.iloc[k]["Price"]
            },
            {
                "symbol": "SP500.45",
                "name": "Information Technology",
                "price": self.app.it_data.iloc[k]["Price"]
            },
            {
                "symbol": "SP500.15",
                "name": "Materials",
                "price": self.app.materials_data.iloc[k]["Price"]
            },
            {
                "symbol": "SP500.60",
                "name": "Real Estate",
                "price": self.app.real_estate_data.iloc[k]["Price"]
            },
            {
                "symbol": "SP500.50",
                "name": "Telecom Services",
                "price": self.app.telecom_data.iloc[k]["Price"]
            },
            {
                "symbol": "SP500.55",
                "name": "Utilities",
                "price": self.app.utilities_data.iloc[k]["Price"]
            },
        ]
        for i in range(11):
            buy_btn = QPushButton("BUY", self)
            buy_btn.setGeometry(840, 30 + i * 30, 50, 20)
            buy_btn.clicked.connect(lambda: self.app.buy_stock(stocks[i]))

    def set_table_values(self):
        # Set the table values
        for i in range(len(self.headers)):
            if i == 0:
                self.table.setItem(0, i, QTableWidgetItem("SP500.25"))
                self.table.setItem(1, i, QTableWidgetItem("SP500.30"))
                self.table.setItem(2, i, QTableWidgetItem("SP500.10"))
                self.table.setItem(3, i, QTableWidgetItem("SP500.40"))
                self.table.setItem(4, i, QTableWidgetItem("SP500.35"))
                self.table.setItem(5, i, QTableWidgetItem("SP500.20"))
                self.table.setItem(6, i, QTableWidgetItem("SP500.45"))
                self.table.setItem(7, i, QTableWidgetItem("SP500.15"))
                self.table.setItem(8, i, QTableWidgetItem("SP500.60"))
                self.table.setItem(9, i, QTableWidgetItem("SP500.50"))
                self.table.setItem(10, i, QTableWidgetItem("SP500.55"))
            elif i == 1:
                self.table.setItem(0, i, QTableWidgetItem("Consumer Discretionary"))
                self.table.setItem(1, i, QTableWidgetItem("Consumer Staples"))
                self.table.setItem(2, i, QTableWidgetItem("Energy"))
                self.table.setItem(3, i, QTableWidgetItem("Financials"))
                self.table.setItem(4, i, QTableWidgetItem("Healthcare"))
                self.table.setItem(5, i, QTableWidgetItem("Industrials"))
                self.table.setItem(6, i, QTableWidgetItem("Information Technology"))
                self.table.setItem(7, i, QTableWidgetItem("Materials"))
                self.table.setItem(8, i, QTableWidgetItem("Real Estate"))
                self.table.setItem(9, i, QTableWidgetItem("Telecom Services"))
                self.table.setItem(10, i, QTableWidgetItem("Utilities"))
            else:
                k = len(self.app.it_data.columns) - self.app.day
                consumer_dis = QTableWidgetItem(str(self.app.consumer_dis_data.iloc[k][self.headers[i]]))
                self.set_item_color(consumer_dis)
                self.table.setItem(0, i, consumer_dis)

                consumer_stp = QTableWidgetItem(str(self.app.consumer_stp_data.iloc[k][self.headers[i]]))
                self.set_item_color(consumer_stp)
                self.table.setItem(1, i, consumer_stp)

                energy = QTableWidgetItem(str(self.app.energy_data.iloc[k][self.headers[i]]))
                self.set_item_color(energy)
                self.table.setItem(2, i, energy)

                finance = QTableWidgetItem(str(self.app.finance_data.iloc[k][self.headers[i]]))
                self.set_item_color(finance)
                self.table.setItem(3, i, finance)

                healthcare = QTableWidgetItem(str(self.app.healthcare_data.iloc[k][self.headers[i]]))
                self.set_item_color(healthcare)
                self.table.setItem(4, i, healthcare)

                industrials = QTableWidgetItem(str(self.app.industrials_data.iloc[k][self.headers[i]]))
                self.set_item_color(industrials)
                self.table.setItem(5, i, industrials)

                it = QTableWidgetItem(str(self.app.it_data.iloc[k][self.headers[i]]))
                self.set_item_color(it)
                self.table.setItem(6, i, it)

                materials = QTableWidgetItem(str(self.app.materials_data.iloc[k][self.headers[i]]))
                self.set_item_color(materials)
                self.table.setItem(7, i, materials)

                real_estate = QTableWidgetItem(str(self.app.real_estate_data.iloc[k][self.headers[i]]))
                self.set_item_color(real_estate)
                self.table.setItem(8, i, real_estate)

                telecom = QTableWidgetItem(str(self.app.telecom_data.iloc[k][self.headers[i]]))
                self.set_item_color(telecom)
                self.table.setItem(9, i, telecom)

                utilities = QTableWidgetItem(str(self.app.utilities_data.iloc[k][self.headers[i]]))
                self.set_item_color(utilities)
                self.table.setItem(10, i, utilities)

    def set_item_color(self, item):
        if "-" in item.text():
            item.setForeground(QBrush(QColor(181, 26, 40)))
        elif "%" in item.text():
            item.setForeground(QBrush(QColor(0, 172, 78)))
