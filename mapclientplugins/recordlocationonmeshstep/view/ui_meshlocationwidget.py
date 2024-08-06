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
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxVisibility)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBoxSurfacesVisibility = QCheckBox(self.groupBoxVisibility)
        self.checkBoxSurfacesVisibility.setObjectName(u"checkBoxSurfacesVisibility")
        self.checkBoxSurfacesVisibility.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBoxSurfacesVisibility)

        self.checkBoxLinesVisibility = QCheckBox(self.groupBoxVisibility)
        self.checkBoxLinesVisibility.setObjectName(u"checkBoxLinesVisibility")
        self.checkBoxLinesVisibility.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBoxLinesVisibility)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBoxNodeSize = QDoubleSpinBox(self.groupBoxVisibility)
        self.spinBoxNodeSize.setObjectName(u"spinBoxNodeSize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBoxNodeSize.sizePolicy().hasHeightForWidth())
        self.spinBoxNodeSize.setSizePolicy(sizePolicy1)
        self.spinBoxNodeSize.setDecimals(4)
        self.spinBoxNodeSize.setMaximum(99999.990000000005239)
        self.spinBoxNodeSize.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.spinBoxNodeSize, 0, 1, 1, 1)

        self.labelNodeSize = QLabel(self.groupBoxVisibility)
        self.labelNodeSize.setObjectName(u"labelNodeSize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelNodeSize.sizePolicy().hasHeightForWidth())
        self.labelNodeSize.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.labelNodeSize, 0, 0, 1, 1)

        self.pushButtonResetNodeSize = QPushButton(self.groupBoxVisibility)
        self.pushButtonResetNodeSize.setObjectName(u"pushButtonResetNodeSize")

        self.gridLayout.addWidget(self.pushButtonResetNodeSize, 0, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelAxisScale = QLabel(self.groupBoxVisibility)
        self.labelAxisScale.setObjectName(u"labelAxisScale")
        sizePolicy2.setHeightForWidth(self.labelAxisScale.sizePolicy().hasHeightForWidth())
        self.labelAxisScale.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.labelAxisScale)

        self.spinBoxAxisScale = QDoubleSpinBox(self.groupBoxVisibility)
        self.spinBoxAxisScale.setObjectName(u"spinBoxAxisScale")
        sizePolicy1.setHeightForWidth(self.spinBoxAxisScale.sizePolicy().hasHeightForWidth())
        self.spinBoxAxisScale.setSizePolicy(sizePolicy1)
        self.spinBoxAxisScale.setDecimals(4)
        self.spinBoxAxisScale.setMaximum(99999.990000000005239)
        self.spinBoxAxisScale.setSingleStep(0.100000000000000)
        self.spinBoxAxisScale.setValue(1.000000000000000)

        self.horizontalLayout_4.addWidget(self.spinBoxAxisScale)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBoxVisibility)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.checkBoxLinesVisibility.setText(QCoreApplication.translate("MeshLocationWidget", u"Lines", None))
        self.labelNodeSize.setText(QCoreApplication.translate("MeshLocationWidget", u"Node Size:", None))
#if QT_CONFIG(tooltip)
        self.pushButtonResetNodeSize.setToolTip(QCoreApplication.translate("MeshLocationWidget", u"Reset node size to appropriate size for current mesh.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonResetNodeSize.setText(QCoreApplication.translate("MeshLocationWidget", u"Reset", None))
        self.labelAxisScale.setText(QCoreApplication.translate("MeshLocationWidget", u"Axis Scale:", None))
        self.groupBoxView.setTitle(QCoreApplication.translate("MeshLocationWidget", u"View", None))
        self.pushButtonViewAll.setText(QCoreApplication.translate("MeshLocationWidget", u"View All", None))
        self.groupBoxGeneral.setTitle(QCoreApplication.translate("MeshLocationWidget", u"General", None))
        self.pushButtonContinue.setText(QCoreApplication.translate("MeshLocationWidget", u"Continue", None))
    # retranslateUi

