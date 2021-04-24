from PyQt5.QtWidgets import *
from qtpy.QtWidgets import QLabel
from qtpy.QtCore import Qt
from examples.example_calculator.calc_conf import register_node, OP_NODE_OUTPUT
from examples.example_calculator.calc_node_base import CalcNode, CalcGraphicsNode
from nodeeditor.node_content_widget import QDMNodeContentWidget
# from examples.example_calculator.PP import Example
# from examples.example_calculator.calc_window import CalculatorWindow

class CalcOutputContent(QDMNodeContentWidget):
    def initUI(self):
        # self.layout=CalculatorWindow.jib_button()
        # self.setLayout(self.layout)
        self.lbl = QLabel("Master", self)
        self.lbl.setAlignment(Qt.AlignLeft)
        self.lbl.setObjectName(self.node.content_label_objname)
        # self.layout = Example.initUI(self)

@register_node(OP_NODE_OUTPUT)
class CalcNode_Output(CalcNode):
    icon = "icons/out.png"
    op_code = OP_NODE_OUTPUT
    op_title = "Master"
    content_label_objname = "calc_node_output"

    def __init__(self, scene):
        super().__init__(scene)

    def initInnerClasses(self):
        self.content = CalcOutputContent(self)
        self.grNode = CalcGraphicsNode(self)

    # def evalImplementation(self):
    #     input_node = self.getInput(0)
    #     if not input_node:
    #         self.grNode.setToolTip("Input is not connected")
    #         self.markInvalid()
    #         return
    #
    #     val = input_node.eval()
    #
    #     if val is None:
    #         self.grNode.setToolTip("Input is NaN")
    #         self.markInvalid()
    #         return
    #
    #     self.content.lbl.setText("%d" % val)
    #     self.markInvalid(False)
    #     self.markDirty(False)
    #     self.grNode.setToolTip("")
    #
    #     return val



#Ok lezemna linna n3awdou ili fil input ema nbedlou il essem nrodouh MASTER w fard wa9t n7awlou il
#check boxes n7otohom fi QHLayoutBox wa7adhom bech nwalliw anything yet7at fih yetzed lil jme3a lkoll
