from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox
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

    def initUI(self):

        # self.layout1=CalculatorWindow.jib_button(self)
        # self.setLayout(self.layout)
        # box1=QHBoxLayout()
        # box1.addWidget(self.layout1)
        self.edit = QLineEdit("", self)
        self.edit.setAlignment(Qt.AlignLeft)
        self.edit.setPlaceholderText("type name ")
        self.edit.setObjectName(self.node.content_label_objname)
        # you can use this backround for the checkbox ye seif :QCheckBox{ spacing: 5px; outline: none;color: #bbb; margin-bottom: 2px;}

    def zz(self):
        qq=QHBoxLayout()
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
