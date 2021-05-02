from qtpy.QtGui import QImage
from qtpy.QtCore import QRectF
from qtpy.QtWidgets import QLabel

from nodeeditor.node_node import Node
from nodeeditor.node_content_widget import QDMNodeContentWidget
from nodeeditor.node_graphics_node import QDMGraphicsNode
from nodeeditor.utils import dumpException


class CalcGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 170
        self.height = 200
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage("icons/status_icons.png")



class CalcContent(QDMNodeContentWidget):
    def initUI(self):
        lbl = QLabel(self.node.content_label, self)
        lbl.setObjectName(self.node.content_label_objname)

class CalcNode(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CalcGraphicsNode
    NodeContent_class = CalcContent

    def __init__(self, scene ):
        super().__init__(scene, self.__class__.op_title)

        self.value = None

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
#        self.markDirty()
#        self.eval()
#

    # def serialize(self):
    #     res = super().serialize()
    #     res['op_code'] = self.__class__.op_code
    #     return res
    #
    # def deserialize(self, data, hashmap={}, restore_id=True):
    #     res = super().deserialize(data, hashmap, restore_id)
    #     print("Deserialized CalcNode '%s'" % self.__class__.__name__, "res:", res)
    #     return res