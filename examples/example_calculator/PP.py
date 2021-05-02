# from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel, QCheckBox,
#                              QHBoxLayout, QVBoxLayout, QButtonGroup)
# import sys
# # from examples.example_calculator.calc_window import CalculatorWindow
# from typing import TYPE_CHECKING
#
#
# # if TYPE_CHECKING:
# #     from examples.example_calculator.nodes.input import CalcInputContent
# class Example(QWidget):
#
#     def __init__(self,c):
#         super().__init__()
#         self.showDialog()
#     # def initUI(self):
#     #     # # Add button
#     #     CalculatorWindow.jib_button(self)
#         # self.btn = QPushButton('Show Input Dialog', self)
#         # self.btn.move(30, 20)
#         # self.btn.clicked.connect(self.showDialog)
#
#         # Add label
#         # self.le = QVBoxLayout(self)
#         # self.le.move(30, 62)
#         # self.le.resize(400,22)
#         # self.cs_group = QButtonGroup(self)
#         # self.setGeometry(300, 300, 290, 150)
#         # self.setWindowTitle('Input dialog')
#         # self.show()
#
#
#         self.c=QHBoxLayout(self)
#         self.c.addWidget(self.TableList)
#     def showDialog(self):
#         # f = open("guru99.txt", "a+")
#         self.TableList= []
#
#         while True:
#             text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter text:',)
#             if ok:
#                 cbtn=QPushButton(f'{str(text)}')
#                 cbtn.setStyleSheet("QCheckBox {     spacing: 5px;     outline: none;     color: #bbb;     margin-bottom: 2px; }")
#                 self.TableList.append(cbtn)
#                 # self.cs_group.addButton(cbtn)
#                 # f.write(cbtn)
#                 # self.qq=QHBoxLayout(self)
#                 # self.qq.addWidget(cbtn)
#                 # c=CalcInputContent.zz(self.qq)
#
#             else:
#                 # f.close()
#                 break
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = Example()
# #     sys.exit(app.exec_())