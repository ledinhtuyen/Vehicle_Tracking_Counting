# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_App(object):
    def setupUi(self, App):
        if not App.objectName():
            App.setObjectName(u"App")
        App.resize(1313, 720)
        App.setMinimumSize(QSize(1313, 720))
        App.setMaximumSize(QSize(1315, 720))
        self.gridLayout_2 = QGridLayout(App)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.labelVideo1 = QLabel(App)
        self.labelVideo1.setObjectName(u"labelVideo1")
        self.labelVideo1.setMinimumSize(QSize(640, 384))
        self.labelVideo1.setMaximumSize(QSize(640, 384))
        self.labelVideo1.setStyleSheet(u"background-color: lightgray; border: 2px solid gray; border-radius: 10px; padding: 5px;\n"
"                           font-size: 16px; font-weight: bold;")
        self.labelVideo1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelVideo1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.startVideo1 = QPushButton(App)
        self.startVideo1.setObjectName(u"startVideo1")
        self.startVideo1.setStyleSheet(u"QPushButton {\n"
"  background-color: #4CAF50;\n"
"  border: none;\n"
"  border-radius: 50px;\n"
"  color: #fff;\n"
"  padding: 12px 32px;\n"
"  font-size: 20px;\n"
"  font-weight: bold;\n"
"  text-transform: uppercase;\n"
"  letter-spacing: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #66BB6A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #43A047;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.startVideo1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.checkBoxTrack1 = QCheckBox(App)
        self.checkBoxTrack1.setObjectName(u"checkBoxTrack1")
        self.checkBoxTrack1.setStyleSheet(u"QCheckBox {\n"
"  color: #333;\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  background-color: transparent;\n"
"  padding-left: 24px;\n"
"  padding-top: 16px;\n"
"  padding-bottom: 16px;\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 20px;\n"
"  height: 20px;\n"
"  border: 2px solid #ccc;\n"
"  border-radius: 5px;\n"
"  background-color: #fff;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"  border-color: #6ab5ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  border-color: #6ab5ff;\n"
"  background-color: #6ab5ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"  border-color: #2f80ff;\n"
"  background-color: #2f80ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"  border-color: #ccc;\n"
"  background-color: #f7f7f7;\n"
"  opacity: 0.6;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"  border-color: #ccc;\n"
"  background-color: #ccc;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.checkBoxTrack1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.checkBoxCount1 = QCheckBox(App)
        self.checkBoxCount1.setObjectName(u"checkBoxCount1")
        self.checkBoxCount1.setStyleSheet(u"QCheckBox {\n"
"  color: #333;\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  background-color: transparent;\n"
"  padding-left: 24px;\n"
"  padding-top: 16px;\n"
"  padding-bottom: 16px;\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 20px;\n"
"  height: 20px;\n"
"  border: 2px solid #ccc;\n"
"  border-radius: 5px;\n"
"  background-color: #fff;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"  border-color: #6ab5ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  border-color: #6ab5ff;\n"
"  background-color: #6ab5ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"  border-color: #2f80ff;\n"
"  background-color: #2f80ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"  border-color: #ccc;\n"
"  background-color: #f7f7f7;\n"
"  opacity: 0.6;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"  border-color: #ccc;\n"
"  background-color: #ccc;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.checkBoxCount1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.labelVideo2 = QLabel(App)
        self.labelVideo2.setObjectName(u"labelVideo2")
        self.labelVideo2.setMinimumSize(QSize(640, 384))
        self.labelVideo2.setMaximumSize(QSize(640, 384))
        self.labelVideo2.setStyleSheet(u"background-color: lightgray; border: 2px solid gray; border-radius: 10px; padding: 5px;font-size: 16px; font-weight: bold;")
        self.labelVideo2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.labelVideo2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.startVideo2 = QPushButton(App)
        self.startVideo2.setObjectName(u"startVideo2")
        self.startVideo2.setStyleSheet(u"QPushButton {\n"
"  background-color: #4CAF50;\n"
"  border: none;\n"
"  border-radius: 50px;\n"
"  color: #fff;\n"
"  padding: 12px 32px;\n"
"  font-size: 20px;\n"
"  font-weight: bold;\n"
"  text-transform: uppercase;\n"
"  letter-spacing: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #66BB6A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #43A047;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.startVideo2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.checkBoxTrack2 = QCheckBox(App)
        self.checkBoxTrack2.setObjectName(u"checkBoxTrack2")
        self.checkBoxTrack2.setStyleSheet(u"QCheckBox {\n"
"  color: #333;\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  background-color: transparent;\n"
"  padding-left: 24px;\n"
"  padding-top: 16px;\n"
"  padding-bottom: 16px;\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 20px;\n"
"  height: 20px;\n"
"  border: 2px solid #ccc;\n"
"  border-radius: 5px;\n"
"  background-color: #fff;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"  border-color: #6ab5ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  border-color: #6ab5ff;\n"
"  background-color: #6ab5ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"  border-color: #2f80ff;\n"
"  background-color: #2f80ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"  border-color: #ccc;\n"
"  background-color: #f7f7f7;\n"
"  opacity: 0.6;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"  border-color: #ccc;\n"
"  background-color: #ccc;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.checkBoxTrack2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.checkBoxCount2 = QCheckBox(App)
        self.checkBoxCount2.setObjectName(u"checkBoxCount2")
        self.checkBoxCount2.setStyleSheet(u"QCheckBox {\n"
"  color: #333;\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  background-color: transparent;\n"
"  padding-left: 24px;\n"
"  padding-top: 16px;\n"
"  padding-bottom: 16px;\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  width: 20px;\n"
"  height: 20px;\n"
"  border: 2px solid #ccc;\n"
"  border-radius: 5px;\n"
"  background-color: #fff;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"  border-color: #6ab5ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  border-color: #6ab5ff;\n"
"  background-color: #6ab5ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"  border-color: #2f80ff;\n"
"  background-color: #2f80ff;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"  border-color: #ccc;\n"
"  background-color: #f7f7f7;\n"
"  opacity: 0.6;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"  border-color: #ccc;\n"
"  background-color: #ccc;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.checkBoxCount2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.retranslateUi(App)

        QMetaObject.connectSlotsByName(App)
    # setupUi

    def retranslateUi(self, App):
        App.setWindowTitle(QCoreApplication.translate("App", u"Vehicle Tracking", None))
        self.labelVideo1.setText(QCoreApplication.translate("App", u"Cick to select video 1", None))
        self.startVideo1.setText(QCoreApplication.translate("App", u"Start Video 1", None))
        self.checkBoxTrack1.setText(QCoreApplication.translate("App", u"Track Video 1", None))
        self.checkBoxCount1.setText(QCoreApplication.translate("App", u"Count Video 1", None))
        self.labelVideo2.setText(QCoreApplication.translate("App", u"Click to select video 2", None))
        self.startVideo2.setText(QCoreApplication.translate("App", u"Start Video 2", None))
        self.checkBoxTrack2.setText(QCoreApplication.translate("App", u"Track Video 2", None))
        self.checkBoxCount2.setText(QCoreApplication.translate("App", u"Count Video 2", None))
    # retranslateUi

