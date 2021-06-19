from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QSize


class AssetsDialog(QDialog):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.setWindowTitle("Assets")
        self.setMinimumSize(QSize(969, 619))

        self.sellbtn3 = QtWidgets.QPushButton(self)
        self.qty3 = QtWidgets.QLabel(self)
        self.qty2 = QtWidgets.QLabel(self)
        self.qty1 = QtWidgets.QLabel(self)
        self.value3 = QtWidgets.QLabel(self)
        self.value2 = QtWidgets.QLabel(self)
        self.value1 = QtWidgets.QLabel(self)
        self.item3 = QtWidgets.QLabel(self)
        self.item2 = QtWidgets.QLabel(self)
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.label_9 = QtWidgets.QLabel(self)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_7 = QtWidgets.QLabel(self)
        self.label_6 = QtWidgets.QLabel(self)
        self.label_5 = QtWidgets.QLabel(self)
        self.item1 = QtWidgets.QLabel(self)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_4 = QtWidgets.QLabel(self)
        self.label = QtWidgets.QLabel(self)
        self.sellbtn2 = QtWidgets.QPushButton(self)
        self.price1 = QtWidgets.QLabel(self)
        self.price2 = QtWidgets.QLabel(self)
        self.price3 = QtWidgets.QLabel(self)
        self.setupUi()

    def setupUi(self):
        self.sellbtn2.setGeometry(QtCore.QRect(710, 150, 121, 31))
        self.sellbtn2.setObjectName("sellbtn2")
        self.label.setGeometry(QtCore.QRect(420, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2.setGeometry(QtCore.QRect(100, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.item1.setGeometry(QtCore.QRect(100, 120, 141, 20))
        self.item1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.item1.setObjectName("item1")
        self.label_5.setGeometry(QtCore.QRect(430, 310, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6.setGeometry(QtCore.QRect(110, 380, 421, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7.setGeometry(QtCore.QRect(110, 420, 111, 16))
        self.label_7.setObjectName("label_7")
        self.label_8.setGeometry(QtCore.QRect(110, 460, 101, 16))
        self.label_8.setObjectName("label_8")
        self.label_9.setGeometry(QtCore.QRect(110, 500, 81, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_3.setGeometry(QtCore.QRect(710, 410, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4.setGeometry(QtCore.QRect(710, 450, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5.setGeometry(QtCore.QRect(710, 490, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.item2.setGeometry(QtCore.QRect(100, 160, 171, 21))
        self.item2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.item2.setObjectName("item2")
        self.item3.setGeometry(QtCore.QRect(100, 200, 191, 16))
        self.item3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.item3.setObjectName("item3")
        self.value1.setGeometry(QtCore.QRect(320, 120, 131, 20))
        self.value1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.value1.setObjectName("value1")
        self.value2.setGeometry(QtCore.QRect(320, 160, 131, 16))
        self.value2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.value2.setObjectName("value2")
        self.value3.setGeometry(QtCore.QRect(320, 200, 121, 20))
        self.value3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.value3.setObjectName("value3")
        self.qty1.setGeometry(QtCore.QRect(540, 110, 81, 16))
        self.qty1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qty1.setObjectName("qty1")
        self.qty2.setGeometry(QtCore.QRect(540, 160, 81, 16))
        self.qty2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qty2.setObjectName("qty2")
        self.qty3.setGeometry(QtCore.QRect(540, 200, 81, 16))
        self.qty3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qty3.setObjectName("qty3")
        self.sellbtn3.setGeometry(QtCore.QRect(710, 190, 121, 31))
        self.sellbtn3.setObjectName("sellbtn3")
        self.label_3.setGeometry(QtCore.QRect(320, 80, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4.setGeometry(QtCore.QRect(550, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.price1.setGeometry(QtCore.QRect(310, 420, 111, 16))
        self.price1.setObjectName("price1")
        self.price2.setGeometry(QtCore.QRect(310, 460, 111, 16))
        self.price2.setObjectName("price2")
        self.price3.setGeometry(QtCore.QRect(310, 500, 111, 16))
        self.price3.setObjectName("price3")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.sellbtn2.setText(_translate("Dialog", "Sell"))
        self.label.setText(_translate("Dialog", "My Assets"))
        self.label_2.setText(_translate("Dialog", "Item"))
        self.item1.setText(_translate("Dialog", "Cash"))
        self.label_5.setText(_translate("Dialog", "Shop"))
        self.label_6.setText(_translate("Dialog", "Item                                          Price"))
        self.label_7.setText(_translate("Dialog", "Car"))
        self.label_8.setText(_translate("Dialog", "Insurance"))
        self.label_9.setText(_translate("Dialog", "Land"))
        self.pushButton_3.setText(_translate("Dialog", "Buy"))
        self.pushButton_4.setText(_translate("Dialog", "Buy"))
        self.pushButton_5.setText(_translate("Dialog", "Buy"))
        self.item2.setText(_translate("Dialog", "Stock (Healthcare)"))
        self.item3.setText(_translate("Dialog", "House"))
        self.value1.setText(_translate("Dialog", "$2000"))
        self.value2.setText(_translate("Dialog", "$100/stock"))
        self.value3.setText(_translate("Dialog", "$1.2M"))
        self.qty1.setText(_translate("Dialog", "-"))
        self.qty2.setText(_translate("Dialog", "20"))
        self.qty3.setText(_translate("Dialog", "1"))
        self.sellbtn3.setText(_translate("Dialog", "Sell"))
        self.label_3.setText(_translate("Dialog", "Market Value"))
        self.label_4.setText(_translate("Dialog", "Quantity"))
        self.price1.setText(_translate("Dialog", "$16K"))
        self.price2.setText(_translate("Dialog", "$300"))
        self.price3.setText(_translate("Dialog", "Variable"))
