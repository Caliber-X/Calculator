# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiTnmIOq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(470, 386)
        Frame.setAcceptDrops(False)
        self.toolButton = QToolButton(Frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(250, 120, 75, 23))
        self.checkBox = QCheckBox(Frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(150, 70, 71, 41))

        self.retranslateUi(Frame)
        self.checkBox.stateChanged.connect(self.toolButton.toggle)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.toolButton.setText(QCoreApplication.translate("Frame", u"OK", None))
        self.checkBox.setText(QCoreApplication.translate("Frame", u"CheckBox", None))
    # retranslateUi

