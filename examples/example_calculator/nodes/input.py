from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QButtonGroup
from qtpy.QtWidgets import QLineEdit
from qtpy.QtCore import Qt

import nodeeditor.node_editor_widget
from examples.example_calculator.calc_conf import register_node, OP_NODE_INPUT
from examples.example_calculator.calc_node_base import CalcNode, CalcGraphicsNode
from nodeeditor.node_content_widget import QDMNodeContentWidget
from nodeeditor.utils import dumpException
# from examples.example_calculator.PP import Example
from nodeeditor.node_scene import Scene
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
    # from examples.example_calculator.calc_window import CalculatorWindow
class CalcInputContent(QDMNodeContentWidget):
    # def openDialog(self):
    #     self.dialog=Example(self)
    #     self.dialog.c(self)
    def initUI(self):

        # self.dialog(self)
        # self.layout1=CalculatorWindow.jib_button(self)
        # self.setLayout(self.layout)
        # box1=QHBoxLayout()
        # box1.addWidget(self.layout1)
        self.edit = QLineEdit("", self)
        self.edit.setAlignment(Qt.AlignLeft)
        self.edit.setPlaceholderText("type name ")
        self.edit.setObjectName(self.node.content_label_objname)
        qb1=QPushButton("X")
        qb1.setCheckable(True)
        qb1.setStyleSheet(
                             "QPushButton::checked"
                             "{"
                             "background-color : red;"
                             "}"
                             )
        # qb1.setStyleSheet("QPushButton {background-color: blue;}")
        qb2=QPushButton("Y")
        qb3=QPushButton("Z")
        qb2.setCheckable(True)
        qb3.setCheckable(True)
        layout1=QVBoxLayout()
        layout1.addWidget(self.edit)
        layout1.addWidget(qb1)
        layout1.addWidget(qb2)
        layout1.addWidget(qb3)
        self.setLayout(layout1)
        # cs_group = QButtonGroup()
        # cs_group.addButton(qb1)
        # cs_group.addButton(qb2)
        # cs_group.addButton(qb3)
        # self.layout2.addWidget(cs_group)
        # self.layout2.addWidget(self.edit)
        # self.setLayout(self.layout2)

        # you can use this backround for the checkbox ye seif :QCheckBox{ spacing: 5px; outline: none;color: #bbb; margin-bottom: 2px;}

    # def serialize(self):
    #     res = super().serialize()
    #     res['value'] = self.edit.text()
    #     return res
    #
    # def deserialize(self, data, hashmap={}):
    #     res = super().deserialize(data, hashmap)
    #     try:
    #         value = data['value']
    #         self.edit.setText(value)
    #         return True & res
    #     except Exception as e:
    #         dumpException(e)
    #     return res
    #


@register_node(OP_NODE_INPUT)
class CalcNode_Input(CalcNode):
    icon = "icons/in.png"
    op_code = OP_NODE_INPUT
    op_title = "name"
    content_label_objname = "calc_node_input"

    def __init__(self, scene):
        super().__init__(scene)
#        self.eval()




    def initInnerClasses(self):
        self.content = CalcInputContent(self)
        self.grNode = CalcGraphicsNode(self)
        self.content.edit.textChanged.connect(self.onInputChanged)
