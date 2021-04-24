from PyQt5.QtWidgets import QWidget, QHBoxLayout

from examples.example_calculator.calc_window import CalculatorWindow
class Example2(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # # Add button
        self.bitch=CalculatorWindow.jib_button(self)
    def jibou(self):
        box1=QHBoxLayout()

        box1.addWidget(self.bitch)
        self.setLayout(box1)
        # self.show()