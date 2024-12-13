from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import *

app = QtWidgets.QApplication([])
ui = uic.loadUi('design.ui')
ui.setWindowTitle('Простой редактор текста')


def Open():
    adress = ui.Adress.displayText()
    file = open(adress, 'r', encoding='utf-8')
    text = file.read()
    ui.textEdit.setText(text)
    file.close


def Save():
    name_raw = ui.Name.displayText()
    name = name_raw + '.txt'
    SFile = open(name, 'w', encoding='utf-8')
    EdText = ui.textEdit.toPlainText()
    SFile.write(EdText)
    SFile.close


def Close():
    ui.textEdit.setText('')

ui.Open.clicked.connect(Open)
ui.Save.clicked.connect(Save)
ui.Close.clicked.connect(Close)

ui.show()
app.exec()
