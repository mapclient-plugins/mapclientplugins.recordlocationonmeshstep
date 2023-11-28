# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meshlocationwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from cmlibs.widgets.basesceneviewerwidget import BaseSceneviewerWidget

class Ui_MeshLocationWidget(object):
    def setupUi(self, MeshLocationWidget):
        if not MeshLocationWidget.objectName():
            MeshLocationWidget.setObjectName(u"MeshLocationWidget")
        MeshLocationWidget.resize(884, 765)
        self.horizontalLayout_3 = QHBoxLayout(MeshLocationWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutHeader = QHBoxLayout()
        self.horizontalLayoutHeader.setObjectName(u"horizontalLayoutHeader")
        self.labelMeshLocation = QLabel(MeshLocationWidget)
        self.labelMeshLocation.setObjectName(u"labelMeshLocation")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMeshLocation.sizePolicy().hasHeightForWidth())
        self.labelMeshLocation.setSizePolicy(sizePolicy)

        self.horizontalLayoutHeader.addWidget(self.labelMeshLocation)

        self.labelMeshLocationIdentifier = QLabel(MeshLocationWidget)
        self.labelMeshLocationIdentifier.setObjectName(u"labelMeshLocationIdentifier")

        self.horizontalLayoutHeader.addWidget(self.labelMeshLocationIdentifier)


        self.verticalLayout.addLayout(self.horizontalLayoutHeader)

        self.line = QFrame(MeshLocationWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.groupBoxGraphics = QGroupBox(MeshLocationWidget)
        self.groupBoxGraphics.setObjectName(u"groupBoxGraphics")
        self.verticalLayout_8 = QVBoxLayout(self.groupBoxGraphics)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBoxCoordinateField = QComboBox(self.groupBoxGraphics)
        self.comboBoxCoordinateField.setObjectName(u"comboBoxCoordinateField")

        self.gridLayout_3.addWidget(self.comboBoxCoordinateField, 0, 1, 1, 1)

        self.labelCoordinateField = QLabel(self.groupBoxGraphics)
        self.labelCoordinateField.setObjectName(u"labelCoordinateField")
        self.labelCoordinateField.setMaximumSize(QSize(160, 16777215))

        self.gridLayout_3.addWidget(self.labelCoordinateField, 0, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_3)


        self.verticalLayout.addWidget(self.groupBoxGraphics)

        self.groupBoxMarkers = QGroupBox(MeshLocationWidget)
        self.groupBoxMarkers.setObjectName(u"groupBoxMarkers")
        self.formLayout = QFormLayout(self.groupBoxMarkers)
        self.formLayout.setObjectName(u"formLayout")
        self.listViewMarkers = QListView(self.groupBoxMarkers)
        self.listViewMarkers.setObjectName(u"listViewMarkers")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.listViewMarkers)

        self.labelOrientation = QLabel(self.groupBoxMarkers)
        self.labelOrientation.setObjectName(u"labelOrientation")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelOrientation)

        self.lineEditOrientation = QLineEdit(self.groupBoxMarkers)
        self.lineEditOrientation.setObjectName(u"lineEditOrientation")
        self.lineEditOrientation.setAcceptDrops(False)
        self.lineEditOrientation.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditOrientation)

        self.labelScale = QLabel(self.groupBoxMarkers)
        self.labelScale.setObjectName(u"labelScale")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelScale)

        self.lineEditScale = QLineEdit(self.groupBoxMarkers)
        self.lineEditScale.setObjectName(u"lineEditScale")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditScale)


        self.verticalLayout.addWidget(self.groupBoxMarkers)

        self.groupBoxVisibility = QGroupBox(MeshLocationWidget)
        self.groupBoxVisibility.setObjectName(u"groupBoxVisibility")
        self.verticalLayout_6 = QVBoxLayout(self.groupBoxVisibility)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBoxSurfacesVisibility = QCheckBox(self.groupBoxVisibility)
        self.checkBoxSurfacesVisibility.setObjectName(u"checkBoxSurfacesVisibility")
        self.checkBoxSurfacesVisibility.setChecked(True)

        self.verticalLayout_6.addWidget(self.checkBoxSurfacesVisibility)

        self.checkBoxMeshVisibility = QCheckBox(self.groupBoxVisibility)
        self.checkBoxMeshVisibility.setObjectName(u"checkBoxMeshVisibility")
        self.checkBoxMeshVisibility.setChecked(True)

        self.verticalLayout_6.addWidget(self.checkBoxMeshVisibility)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelNodeSize = QLabel(self.groupBoxVisibility)
        self.labelNodeSize.setObjectName(u"labelNodeSize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelNodeSize.sizePolicy().hasHeightForWidth())
        self.labelNodeSize.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelNodeSize, 0, 0, 1, 1)

        self.spinBoxNodeSize = QDoubleSpinBox(self.groupBoxVisibility)
        self.spinBoxNodeSize.setObjectName(u"spinBoxNodeSize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBoxNodeSize.sizePolicy().hasHeightForWidth())
        self.spinBoxNodeSize.setSizePolicy(sizePolicy2)
        self.spinBoxNodeSize.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.spinBoxNodeSize, 0, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBoxVisibility)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBoxView = QGroupBox(MeshLocationWidget)
        self.groupBoxView.setObjectName(u"groupBoxView")
        self.horizontalLayout = QHBoxLayout(self.groupBoxView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(50, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushButtonViewAll = QPushButton(self.groupBoxView)
        self.pushButtonViewAll.setObjectName(u"pushButtonViewAll")

        self.horizontalLayout.addWidget(self.pushButtonViewAll)

        self.horizontalSpacer_3 = QSpacerItem(50, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.groupBoxView)

        self.groupBoxGeneral = QGroupBox(MeshLocationWidget)
        self.groupBoxGeneral.setObjectName(u"groupBoxGeneral")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBoxGeneral)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButtonContinue = QPushButton(self.groupBoxGeneral)
        self.pushButtonContinue.setObjectName(u"pushButtonContinue")

        self.horizontalLayout_2.addWidget(self.pushButtonContinue)

        self.horizontalSpacer_2 = QSpacerItem(46, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.groupBoxGeneral)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.widgetZinc = BaseSceneviewerWidget(MeshLocationWidget)
        self.widgetZinc.setObjectName(u"widgetZinc")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.widgetZinc.sizePolicy().hasHeightForWidth())
        self.widgetZinc.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.widgetZinc)


        self.retranslateUi(MeshLocationWidget)

        QMetaObject.connectSlotsByName(MeshLocationWidget)
    # setupUi

    def retranslateUi(self, MeshLocationWidget):
        MeshLocationWidget.setWindowTitle(QCoreApplication.translate("MeshLocationWidget", u"Mesh Location", None))
        self.labelMeshLocation.setText(QCoreApplication.translate("MeshLocationWidget", u"Mesh Location - ", None))
        self.labelMeshLocationIdentifier.setText("")
        self.groupBoxGraphics.setTitle(QCoreApplication.translate("MeshLocationWidget", u"Graphics Coordinates", None))
        self.labelCoordinateField.setText(QCoreApplication.translate("MeshLocationWidget", u"Coordinate Field:", None))
        self.groupBoxMarkers.setTitle(QCoreApplication.translate("MeshLocationWidget", u"Markers", None))
        self.labelOrientation.setText(QCoreApplication.translate("MeshLocationWidget", u"Orientation:", None))
        self.labelScale.setText(QCoreApplication.translate("MeshLocationWidget", u"Pixel Scale:", None))
        self.groupBoxVisibility.setTitle(QCoreApplication.translate("MeshLocationWidget", u"Visibility", None))
        self.checkBoxSurfacesVisibility.setText(QCoreApplication.translate("MeshLocationWidget", u"Surfaces", None))
        self.checkBoxMeshVisibility.setText(QCoreApplication.translate("MeshLocationWidget", u"Mesh", None))
        self.labelNodeSize.setText(QCoreApplication.translate("MeshLocationWidget", u"Node Size:", None))
        self.groupBoxView.setTitle(QCoreApplication.translate("MeshLocationWidget", u"View", None))
        self.pushButtonViewAll.setText(QCoreApplication.translate("MeshLocationWidget", u"View All", None))
        self.groupBoxGeneral.setTitle(QCoreApplication.translate("MeshLocationWidget", u"General", None))
        self.pushButtonContinue.setText(QCoreApplication.translate("MeshLocationWidget", u"Continue", None))
    # retranslateUi

