from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Текстовый редактор")
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar() # менюшка

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)


        fileMenu.addAction('Открыть', self.action_clicked)
        fileMenu.addAction('Сохранить', self.action_clicked)
    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Открыть":
            fname = QFileDialog.getOpenFileName(self)[0]
            try:
                f = open(fname, 'r') # чтение файла
                with f:
                    data = f.read()
                    self.text_edit.setText(data)

                f.close()
            except FileNotFoundError:
                print("No such file")

        elif action.text() == "Сохранить":
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                f = open(fname, 'w') # запись файла
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("No such file")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()

























