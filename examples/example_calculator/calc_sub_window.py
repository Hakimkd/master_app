from qtpy.QtGui import QIcon, QPixmap
from qtpy.QtCore import QDataStream, QIODevice, Qt
from qtpy.QtWidgets import QAction, QGraphicsProxyWidget, QMenu

from examples.example_calculator.calc_conf import CALC_NODES, get_class_from_opcode, LISTBOX_MIMETYPE
from nodeeditor.node_editor_widget import NodeEditorWidget
from nodeeditor.node_node import Node
from nodeeditor.utils import dumpException
from examples.example_calculator.PP import Example

DEBUG = False
DEBUG_CONTEXT = False


class CalculatorSubWindow(NodeEditorWidget):
    def __init__(self):
        super().__init__()
        # self.setAttribute(Qt.WA_DeleteOnClose)

        self.setTitle()

        # self.initNewNodeActions()

        self.scene.addHasBeenModifiedListener(self.setTitle)
        # self.scene.history.addHistoryRestoredListener(self.onHistoryRestored)
        self.scene.addDragEnterListener(self.onDragEnter)
        self.scene.addDropListener(self.onDrop)
        self.scene.setNodeClassSelector(self.getNodeClassFromData)

        self._close_event_listeners = []
        Example.showDialog(self)

    def getNodeClassFromData(self, data):
        if 'op_code' not in data: return Node
        return get_class_from_opcode(data['op_code'])
    #
    # def onHistoryRestored(self):
    #     self.doEvalOutputs()

    def fileLoad(self, filename):
        if super().fileLoad(filename):
            self.doEvalOutputs()
            return True

        return False

    # def initNewNodeActions(self):
    #     self.node_actions = {}
    #     keys = list(CALC_NODES.keys())
    #     keys.sort()
    #     for key in keys:
    #         node = CALC_NODES[key]
    #         self.node_actions[node.op_code] = QAction(QIcon(node.icon), node.op_title)
    #         self.node_actions[node.op_code].setData(node.op_code)

    # def initNodesContextMenu(self):
    #     context_menu = QMenu(self)
    #     keys = list(CALC_NODES.keys())
    #     keys.sort()
    #     for key in keys: context_menu.addAction(self.node_actions[key])
    #     return context_menu

    def setTitle(self):
        self.setWindowTitle(self.getUserFriendlyFilename())

    def addCloseEventListener(self, callback):
        self._close_event_listeners.append(callback)

    def closeEvent(self, event):
        for callback in self._close_event_listeners: callback(self, event)

    def onDragEnter(self, event):
        if event.mimeData().hasFormat(LISTBOX_MIMETYPE):
            event.acceptProposedAction()
        else:
            # print(" ... denied drag enter event")
            event.setAccepted(False)

    def onDrop(self, event):
        if event.mimeData().hasFormat(LISTBOX_MIMETYPE):
            eventData = event.mimeData().data(LISTBOX_MIMETYPE)
            dataStream = QDataStream(eventData, QIODevice.ReadOnly)
            pixmap = QPixmap()
            dataStream >> pixmap
            op_code = dataStream.readInt()
            text = dataStream.readQString()

            mouse_position = event.pos()
            scene_position = self.scene.grScene.views()[0].mapToScene(mouse_position)

            if DEBUG: print("GOT DROP: [%d] '%s'" % (op_code, text), "mouse:", mouse_position, "scene:", scene_position)

            try:
                node = get_class_from_opcode(op_code)(self.scene)
                node.setPos(scene_position.x(), scene_position.y())
                self.scene.history.storeHistory("Created node %s" % node.__class__.__name__)
            except Exception as e: dumpException(e)


            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            # print(" ... drop ignored, not requested format '%s'" % LISTBOX_MIMETYPE)
            event.ignore()


    def contextMenuEvent(self, event):
        try:
            item = self.scene.getItemAt(event.pos())
            if DEBUG_CONTEXT: print(item)

            if type(item) == QGraphicsProxyWidget:
                item = item.widget()

            # if hasattr(item, 'node'):
            #     self.handleNodeContextMenu(event)
            #
            # else:
            #     self.handleNewNodeContextMenu(event)

            return super().contextMenuEvent(event)
        except Exception as e: dumpException(e)

    # def handleNodeContextMenu(self, event):
    #     if DEBUG_CONTEXT: print("CONTEXT: NODE")
    #     context_menu = QMenu(self)
    #     markDirtyAct = context_menu.addAction("Mark dhfhdh")
    #     markDirtyDescendantsAct = context_menu.addAction("Mark Descendant Dirty")
    #     markInvalidAct = context_menu.addAction("Mark Invalid")
    #     unmarkInvalidAct = context_menu.addAction("Unmark Invalid")
    #     evalAct = context_menu.addAction("Eval")
    #     action = context_menu.exec_(self.mapToGlobal(event.pos()))
    #
    #     selected = None
    #     item = self.scene.getItemAt(event.pos())
    #     if type(item) == QGraphicsProxyWidget:
    #         item = item.widget()
    #
    #     if hasattr(item, 'node'):
    #         selected = item.node
    #
    #     if DEBUG_CONTEXT: print("got item:", selected)
    #     if selected and action == markDirtyAct: selected.markDirty()
    #     if selected and action == markDirtyDescendantsAct: selected.markDescendantsDirty()
    #     if selected and action == markInvalidAct: selected.markInvalid()
    #     if selected and action == unmarkInvalidAct: selected.markInvalid(False)
    #     if selected and action == evalAct:
    #         val = selected.eval()
    #         if DEBUG_CONTEXT: print("EVALUATED:", val)
    #


    # def finish_new_node_state(self, new_calc_node):
    #     self.scene.doDeselectItems()
    #     new_calc_node.grNode.doSelect(True)
    #     new_calc_node.grNode.onSelected()

    #
    # def handleNewNodeContextMenu(self, event):
    #
    #     if DEBUG_CONTEXT: print("CONTEXT: EMPTY SPACE")
    #     context_menu = self.initNodesContextMenu()
    #     action = context_menu.exec_(self.mapToGlobal(event.pos()))
    #
    #     if action is not None:
    #         new_calc_node = get_class_from_opcode(action.data())(self.scene)
    #         scene_pos = self.scene.getView().mapToScene(event.pos())
    #         new_calc_node.setPos(scene_pos.x(), scene_pos.y())
    #         if DEBUG_CONTEXT: print("Selected node:", new_calc_node)
    #         else:
    #             self.scene.history.storeHistory("Created %s" % new_calc_node.__class__.__name__)
