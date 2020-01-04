from data.sketch.commands.sketch_command import *
from data.sketch.geometry.geom2d_edge import *
from OCC.Core.ElCLib import elclib
from OCC.Core.AIS import AIS_Point
from OCC.Core.Geom2d import Geom2d_CartesianPoint
from OCC.Core.Geom import Geom_CartesianPoint
from enum import Enum


class Line2PAction(Enum):
    Nothing = 0
    Input_FirstPointLine = 1
    Input_SecondPointLine = 2


class Sketch_CommandLine2P(Sketch_Command):
    def __init__(self):
        super(Sketch_CommandLine2P, self).__init__("Line2p.")
        self.myLine2PAction = Line2PAction.Nothing

    def Action(self):
        self.myLine2PAction = Line2PAction.Input_FirstPointLine

    def MouseInputEvent(self, thePnt2d: gp_Pnt2d):

        if self.myPointAction == Line2PAction.Nothing:
            pass
        elif self.myPointAction == Line2PAction.Input_FirstPointLine:
            self.curPnt2d = self.myAnalyserSnap.MouseInputException(thePnt2d, thePnt2d, TangentType.Line_FirstPnt, True)
            self.myFirstgp_Pnt2d = self.curPnt2d
            self.myFirstPoint.SetPnt(elclib.To3d(self.curCoordinateSystem.Ax2(), self.curPnt2d))
            self.myRubberLine.SetPoints(self.myFirstPoint, self.myFirstPoint)
            self.myContext.Display(self.myRubberLine, 0, -1)
        elif self.myPointAction == Line2PAction.Input_SecondPointLine:
            self.curPnt2d = self.myAnalyserSnap.MouseInputException(self.myFirstgp_Pnt2d, thePnt2d,
                                                                    TangentType.Line_SecondPnt, False)
            newGeom2d_Edge = Geom2d_Edge()
            if newGeom2d_Edge.SetPoints(self.myFirstgp_Pnt2d, self.curPnt2d):
                Geom_Point1 = Geom_CartesianPoint(elclib.To3d(self.curCoordinateSystem.Ax2(), self.myFirstgp_Pnt2d))
                Geom_Point2 = Geom_CartesianPoint(elclib.To3d(self.curCoordinateSystem.Ax2(), self.curPnt2d))
                myAIS_Line = AIS_Line(Geom_Point1, Geom_Point2)
                self.AddObject(newGeom2d_Edge, myAIS_Line, Sketch_ObjectGeometryType.LineSketcherObject)

                self.myContext.Display(myAIS_Line, True)
                if self.myPolylineMode:
                    self.myFirstgp_Pnt2d = self.curPnt2d
                    self.myFirstPoint.SetPnt(self.mySecondPoint.Pnt())
                    self.myRubberLine.SetPoints(self.myFirstPoint, self.myFirstPoint)
                    self.myContext.Redisplay(self.myRubberLine)
                else:
                    self.myContext.Remove(self.myRubberLine)
                    self.myLine2PAction = Line2PAction.Input_FirstPointLine

        return False

    def MouseMoveEvent(self, thePnt2d: gp_Pnt2d):
        if self.myPointAction == Line2PAction.Nothing:
            pass
        elif self.myPointAction == Line2PAction.Input_FirstPointLine:
            self.curPnt2d = self.myAnalyserSnap.MouseMoveException(thePnt2d, thePnt2d, TangentType.Line_FirstPnt, True)
        elif self.myPointAction == Line2PAction.Input_SecondPointLine:
            self.curPnt2d = self.myAnalyserSnap.MouseInputException(self.myFirstgp_Pnt2d, thePnt2d,
                                                                    TangentType.Line_SecondPnt, False)
            newGeom2d_Edge = Geom2d_Edge()
            if newGeom2d_Edge.SetPoints(self.myFirstgp_Pnt2d, self.curPnt2d):
                Geom_Point1 = Geom_CartesianPoint(elclib.To3d(self.curCoordinateSystem.Ax2(), self.myFirstgp_Pnt2d))
                Geom_Point2 = Geom_CartesianPoint(elclib.To3d(self.curCoordinateSystem.Ax2(), self.curPnt2d))
                myAIS_Line = AIS_Line(Geom_Point1, Geom_Point2)
                self.AddObject(newGeom2d_Edge, myAIS_Line, Sketch_ObjectGeometryType.LineSketcherObject)

                self.myContext.Display(myAIS_Line, True)
                if self.myPolylineMode:
                    self.myFirstgp_Pnt2d = self.curPnt2d
                    self.myFirstPoint.SetPnt(self.mySecondPoint.Pnt())
                    self.myRubberLine.SetPoints(self.myFirstPoint, self.myFirstPoint)
                    self.myContext.Redisplay(self.myRubberLine)
                else:
                    self.myContext.Remove(self.myRubberLine)
                    self.myLine2PAction = Line2PAction.Input_FirstPointLine

    def CancelEvent(self):
        self.myPointAction = PointAction.Nothing

    def GetTypeOfMethod(self) -> Sketch_ObjectTypeOfMethod:
        return Sketch_ObjectTypeOfMethod.Point_Method