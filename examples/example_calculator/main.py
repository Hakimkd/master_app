import os, sys
from qtpy.QtWidgets import QApplication

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

from examples.example_calculator.calc_window import CalculatorWindow
# from examples.example_calculator.PP2 import Example2

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # print(QStyleFactory.keys())
    app.setStyle('Fusion')
    # Example.showDialog(self)

    # ex=Example2()
    # ex.show()
    wnd = CalculatorWindow()
    wnd.show()

    sys.exit(app.exec_())
