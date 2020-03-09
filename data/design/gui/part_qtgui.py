from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from data.design.part_type import *
from .bezierSurfaceForm import BezierSurfaceForm
from .revolSurfaceForm import RevolSurfaceForm


class Part_QTGUI(object):
    def __init__(self, parent: QMainWindow):
        self.dockWidget = QDockWidget("Tool", parent)
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea)
        parent.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)
        self.form_createBezierSurface = BezierSurfaceForm(self)
        self.form_createRevolSurface = RevolSurfaceForm(self)
        self.forms = [self.form_createBezierSurface, self.form_createRevolSurface]
        self.dockWidget.hide()

    def SetContext(self, theContext):
        for form in self.forms:
            form.SetContext(theContext)

    def SetModel(self, theModel):
        for form in self.forms:
            form.SetModel(theModel)

    def SetGui(self, theActionType: Part_ObjectTypeOfMethod):
        if theActionType == Part_ObjectTypeOfMethod.BezierSurface_Method:
            self.dockWidget.setWidget(self.form_createBezierSurface)
        elif theActionType == Part_ObjectTypeOfMethod.RevolvedSurface_Method:
            self.dockWidget.setWidget(self.form_createRevolSurface)
        elif theActionType == Part_ObjectTypeOfMethod.Nothing_Method:
            self.dockWidget.hide()
        self.dockWidget.show()

    def Hide(self):
        self.dockWidget.hide()