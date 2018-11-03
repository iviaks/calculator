#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
                             QWidget)


class CalculatorWindow(QWidget):
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
        self.layout().addWidget(
            QLineEdit(), 0, 0, 1, 5)

    def add_buttons(self):

        pbSeven = QPushButton('7')
        self.layout().addWidget(pbSeven, 2, 0)
        pbEight = QPushButton('8')
        self.layout().addWidget(pbEight, 2, 1)
        pbNine = QPushButton('9')
        self.layout().addWidget(pbNine, 2, 2)
        pbPlus = QPushButton('+')
        self.layout().addWidget(pbPlus, 2, 4)

        pbFour = QPushButton('4')
        self.layout().addWidget(pbFour, 3, 0)
        pbFive = QPushButton('5')
        self.layout().addWidget(pbFive, 3, 1)
        pbSix = QPushButton('6')
        self.layout().addWidget(pbSix, 3, 2)
        pbMinus = QPushButton('-')
        self.layout().addWidget(pbMinus, 3, 4)

        pbOne = QPushButton('1')
        self.layout().addWidget(pbOne, 4, 0)
        pbTwo = QPushButton('2')
        self.layout().addWidget(pbTwo, 4, 1)
        pbThree = QPushButton('3')
        self.layout().addWidget(pbThree, 4, 2)
        pbMultiply = QPushButton('*')
        self.layout().addWidget(pbMultiply, 4, 4)

        pbPoint = QPushButton('.')
        self.layout().addWidget(pbPoint, 5, 0)
        pbZero = QPushButton('0')
        self.layout().addWidget(pbZero, 5, 1)
        pbEqual = QPushButton('=')
        self.layout().addWidget(pbEqual, 5, 2)
        pbDivision = QPushButton('/')
        self.layout().addWidget(pbDivision, 5, 4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorWindow()
    sys.exit(app.exec_())
