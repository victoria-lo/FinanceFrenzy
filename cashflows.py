from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtGui import QBrush, QColor, QIcon
from PyQt6.QtCore import QSize


class CashflowsDialog(QDialog):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.setWindowTitle("Cashflows")
        self.setMinimumSize(QSize(360, 360))
        self.setWindowIcon(QIcon("./assets/money.png"))

        self.table = QTableWidget(self)
        self.headers = ["Date", "Cashflows", "Net Total"]
        self.table.setColumnCount(len(self.headers))
        # Set the table headers
        self.table.setHorizontalHeaderLabels(self.headers)

        # Set the table values
        self.set_table_values()

        # Resize of the rows and columns based on the content
        self.table.setFixedWidth(360)
        self.table.setFixedHeight(360)
        self.table.show()

    def set_table_values(self):
        self.table.setRowCount(len(self.app.cashflows) + 1)
        net_total = 0
        # Set the table values
        for i in range(len(self.app.cashflows)):
            cashflow_val = self.app.cashflows[i]["value"]
            net_total += cashflow_val
            cf_widget_item = QTableWidgetItem(str(cashflow_val))
            self.set_item_color(cf_widget_item)
            self.table.setItem(i, 0, QTableWidgetItem(str(self.app.cashflows[i]["date"])))
            self.table.setItem(i, 1, cf_widget_item)
            self.table.setItem(i, 2, QTableWidgetItem(""))

        net_widget_item = QTableWidgetItem(str(net_total))
        self.set_item_color(net_widget_item)
        self.table.setItem(len(self.app.cashflows), 2, net_widget_item)

    def set_item_color(self, item):
        if "-" in item.text():
            item.setForeground(QBrush(QColor(181, 26, 40)))
        else:
            item.setForeground(QBrush(QColor(0, 172, 78)))
