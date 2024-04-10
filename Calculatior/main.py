
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from PyQt5.QtWidgets import QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(319, 385)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 361, 50))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet(
            "background-color: rgb(232, 232, 232);")
        self.label_result.setObjectName("label_result")
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(0, 290, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                    "font: 8pt \"Comic Sans MS\";\n"
                                    "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(80, 290, 161, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(255, 129, 56);\n"
                                     "font: 8pt \"Comic Sans MS\";\n"
                                     "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 50, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                 "font: 8pt \"Comic Sans MS\";\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(80, 50, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                 "font: 8pt \"Comic Sans MS\";\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(160, 50, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                 "font: 8pt \"Comic Sans MS\";\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_9.setObjectName("btn_9")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 130, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                 "font: 8pt \"Comic Sans MS\";\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(80, 130, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                 "font: 8pt \"Comic Sans MS\";\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(160, 130, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                 "font: 8pt \"Comic Sans MS\";\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_6.setObjectName("btn_6")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 210, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                 "font: 8pt \"Comic Sans MS\";\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(80, 210, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                 "font: 8pt \"Comic Sans MS\";\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(160, 210, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                 "font: 8pt \"Comic Sans MS\";\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_3.setObjectName("btn_3")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(240, 50, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                    "font: 8pt \"Comic Sans MS\";\n"
                                    "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(240, 130, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                     "font: 8pt \"Comic Sans MS\";\n"
                                     "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_umn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_umn.setGeometry(QtCore.QRect(240, 210, 81, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_umn.setFont(font)
        self.btn_umn.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                   "font: 8pt \"Comic Sans MS\";\n"
                                   "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_umn.setObjectName("btn_umn")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(240, 290, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_del.setFont(font)
        self.btn_del.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                   "font: 8pt \"Comic Sans MS\";\n"
                                   "font: 16pt \"MS Shell Dlg 2\";")
        self.btn_del.setObjectName("btn_del")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_umn.setText(_translate("MainWindow", "*"))
        self.btn_del.setText(_translate("MainWindow", "/"))


# начало изменений ОБРАБОТЧИК ИЗМЕНЕНИЙ

    def add_functions(self):
        self.btn_zero.clicked.connect(
            lambda: self.write_numder(self.btn_zero.text()))
        self.btn_1.clicked.connect(
            lambda: self.write_numder(self.btn_1.text()))
        self.btn_2.clicked.connect(
            lambda: self.write_numder(self.btn_2.text()))
        self.btn_3.clicked.connect(
            lambda: self.write_numder(self.btn_3.text()))
        self.btn_4.clicked.connect(
            lambda: self.write_numder(self.btn_4.text()))
        self.btn_5.clicked.connect(
            lambda: self.write_numder(self.btn_5.text()))
        self.btn_6.clicked.connect(
            lambda: self.write_numder(self.btn_6.text()))
        self.btn_7.clicked.connect(
            lambda: self.write_numder(self.btn_7.text()))
        self.btn_8.clicked.connect(
            lambda: self.write_numder(self.btn_8.text()))
        self.btn_9.clicked.connect(
            lambda: self.write_numder(self.btn_9.text()))
        self.btn_plus.clicked.connect(
            lambda: self.write_numder(self.btn_plus.text()))
        self.btn_minus.clicked.connect(
            lambda: self.write_numder(self.btn_minus.text()))
        self.btn_umn.clicked.connect(
            lambda: self.write_numder(self.btn_umn.text()))
        self.btn_del.clicked.connect(
            lambda: self.write_numder(self.btn_del.text()))

        self.btn_equal.clicked.connect(self.results)

    def write_numder(self, number):
        if self.label_result.text() == "0" or self.is_equal:
            self.label_result.setText(number)
            self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text() + number)

    def results(self):
        res = eval(self.label_result.text())
        self.label_result.setText(str(res))
        self.is_equal = True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
