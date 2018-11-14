#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
                             QWidget)


class CalculatorWindow(QWidget):
    last_number = 0
    new_action = None

    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.add_grid()
        self.add_input()
        self.add_buttons()

        self.show()

    def setup_ui(self):
        self.setWindowTitle('Calculator')

    def add_grid(self):
        self.setLayout(
            QGridLayout()
        )

    def add_input(self):
        input_field = QLineEdit()
        input_field.setReadOnly(True)
        input_field.setText('0')
        self.layout().addWidget(input_field, 0, 0, 1, 5)

    def button_number_clicked(self):
        sender = self.sender()
        input_field = self.layout().itemAtPosition(0, 0).widget()

        if input_field.text() == '0':
            new_value = sender.text()
        else:
            new_value = input_field.text() + sender.text()

        input_field.setText(new_value)

    def button_reset_clicked(self):
        input_field = self.layout().itemAtPosition(0, 0).widget()
        input_field.setText('0')

    def button_operation_clicked(self):
        sender = self.sender()
        input_field = self.layout().itemAtPosition(0, 0).widget()
        self.last_number = int(input_field.text())
        self.new_action = sender.text()
        input_field.setText('0')

    def button_equal_clicked(self):
        input_field = self.layout().itemAtPosition(0, 0).widget()
        result = 0
        if self.new_action == '+':
            result = int(input_field.text()) + self.last_number
        elif self.new_action == '-':
            result = self.last_number - int(input_field.text())
        elif self.new_action == '*':
            result = int(input_field.text()) * self.last_number
        elif self.new_action == '/':
            result = self.last_number / int(input_field.text())

        input_field.setText(str(result))

    def add_buttons(self):

        pbReset = QPushButton('C')
        pbReset.clicked.connect(self.button_reset_clicked)
        self.layout().addWidget(pbReset, 1, 4)

        pbSeven = QPushButton('7')
        pbSeven.clicked.connect(self.button_number_clicked)
        self.layout().addWidget(pbSeven, 2, 0)
        pbEight = QPushButton('8')
        pbEight.clicked.connect(self.button_number_clicked)
        self.layout().addWidget(pbEight, 2, 1)
        pbNine = QPushButton('9')
        pbNine.clicked.connect(self.button_number_clicked)
        self.layout().addWidget(pbNine, 2, 2)
        pbPlus = QPushButton('+')
        pbPlus.clicked.connect(self.button_operation_clicked)
        self.layout().addWidget(pbPlus, 2, 4)

        pbFour = QPushButton('4')
        pbFour.clicked.connect(self.button_number_clicked)
        self.layout().addWidget(pbFour, 3, 0)
        pbFive = QPushButton('5')
        pbFive.clicked.connect(self.button_number_clicked)
        self.layout().addWidget(pbFive, 3, 1)
        pbSix = QPushButton('6')
        pbSix.clicked.connect(self.button_number_clicked)
        self.layout().addWidget(pbSix, 3, 2)
        pbMinus = QPushButton('-')
        pbMinus.clicked.connect(self.button_operation_clicked)
        self.layout().addWidget(pbMinus, 3, 4)

        pbOne = QPushButton('1')
        pbOne.clicked.connect(self.button_number_clicked)
        self.layout().addWidget(pbOne, 4, 0)
        pbTwo = QPushButton('2')
        pbTwo.clicked.connect(self.button_number_clicked)
        self.layout().addWidget(pbTwo, 4, 1)
        pbThree = QPushButton('3')
        pbThree.clicked.connect(self.button_number_clicked)
        self.layout().addWidget(pbThree, 4, 2)
        pbMultiply = QPushButton('*')
        pbMultiply.clicked.connect(self.button_operation_clicked)
        self.layout().addWidget(pbMultiply, 4, 4)

        pbPoint = QPushButton('.')
        self.layout().addWidget(pbPoint, 5, 0)
        pbZero = QPushButton('0')
        pbZero.clicked.connect(self.button_number_clicked)
        self.layout().addWidget(pbZero, 5, 1)
        pbEqual = QPushButton('=')
        pbEqual.clicked.connect(self.button_equal_clicked)
        self.layout().addWidget(pbEqual, 5, 2)
        pbDivision = QPushButton('/')
        pbDivision.clicked.connect(self.button_operation_clicked)
        self.layout().addWidget(pbDivision, 5, 4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorWindow()
    sys.exit(app.exec_())
