# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'curveProperty.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_uiCurveEditor(object):
    def setupUi(self, uiCurveEditor):
        uiCurveEditor.setObjectName("uiCurveEditor")
        uiCurveEditor.resize(693, 448)
        self.verticalLayout = QtWidgets.QVBoxLayout(uiCurveEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(uiCurveEditor)
        self.label_6.setEnabled(True)
        self.label_6.setMinimumSize(QtCore.QSize(75, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.uiCurveOrder = QtWidgets.QDoubleSpinBox(uiCurveEditor)
        self.uiCurveOrder.setMouseTracking(True)
        self.uiCurveOrder.setTabletTracking(True)
        self.uiCurveOrder.setReadOnly(False)
        self.uiCurveOrder.setDecimals(0)
        self.uiCurveOrder.setMinimum(2.0)
        self.uiCurveOrder.setObjectName("uiCurveOrder")
        self.horizontalLayout_6.addWidget(self.uiCurveOrder)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(uiCurveEditor)
        self.label_8.setEnabled(True)
        self.label_8.setMinimumSize(QtCore.QSize(75, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.uiCurveSubdivision = QtWidgets.QDoubleSpinBox(uiCurveEditor)
        self.uiCurveSubdivision.setMouseTracking(True)
        self.uiCurveSubdivision.setTabletTracking(True)
        self.uiCurveSubdivision.setDecimals(0)
        self.uiCurveSubdivision.setMinimum(1.0)
        self.uiCurveSubdivision.setProperty("value", 20.0)
        self.uiCurveSubdivision.setObjectName("uiCurveSubdivision")
        self.horizontalLayout_8.addWidget(self.uiCurveSubdivision)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(uiCurveEditor)
        self.label_7.setEnabled(True)
        self.label_7.setMinimumSize(QtCore.QSize(75, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.uiCurveClamped = QtWidgets.QCheckBox(uiCurveEditor)
        self.uiCurveClamped.setText("")
        self.uiCurveClamped.setTristate(False)
        self.uiCurveClamped.setObjectName("uiCurveClamped")
        self.horizontalLayout_7.addWidget(self.uiCurveClamped)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(uiCurveEditor)
        self.label_9.setEnabled(True)
        self.label_9.setMinimumSize(QtCore.QSize(75, 0))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.uiCurveKnots = QtWidgets.QLineEdit(uiCurveEditor)
        self.uiCurveKnots.setObjectName("uiCurveKnots")
        self.horizontalLayout_9.addWidget(self.uiCurveKnots)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(uiCurveEditor)
        self.label_10.setEnabled(True)
        self.label_10.setMinimumSize(QtCore.QSize(75, 0))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.uiCurveWeights = QtWidgets.QLineEdit(uiCurveEditor)
        self.uiCurveWeights.setObjectName("uiCurveWeights")
        self.horizontalLayout_10.addWidget(self.uiCurveWeights)
        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.retranslateUi(uiCurveEditor)
        QtCore.QMetaObject.connectSlotsByName(uiCurveEditor)

    def retranslateUi(self, uiCurveEditor):
        _translate = QtCore.QCoreApplication.translate
        uiCurveEditor.setWindowTitle(_translate("uiCurveEditor", "Form"))
        self.label_6.setText(_translate("uiCurveEditor", "order"))
        self.label_8.setText(_translate("uiCurveEditor", "subdivision"))
        self.label_7.setText(_translate("uiCurveEditor", "clamped"))
        self.label_9.setText(_translate("uiCurveEditor", "knots"))
        self.label_10.setText(_translate("uiCurveEditor", "weights"))