# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(300, 350)
        MainWindow.setMinimumSize(QtCore.QSize(300, 350))
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 5)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_divide = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_divide.setAutoDefault(True)
        self.pushButton_divide.setDefault(False)
        self.pushButton_divide.setFlat(False)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.gridLayout.addWidget(self.pushButton_divide, 6, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 7, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 7, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 10, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 6, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 7, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 10, 1, 1, 1)
        self.pushButton_subtract = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_subtract.setAutoDefault(True)
        self.pushButton_subtract.setDefault(False)
        self.pushButton_subtract.setFlat(False)
        self.pushButton_subtract.setObjectName("pushButton_subtract")
        self.gridLayout.addWidget(self.pushButton_subtract, 10, 3, 1, 1)
        self.pushButton_dot = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_dot.setAutoDefault(True)
        self.pushButton_dot.setDefault(False)
        self.pushButton_dot.setFlat(False)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.gridLayout.addWidget(self.pushButton_dot, 12, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 6, 2, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_0.setAutoDefault(True)
        self.pushButton_0.setDefault(False)
        self.pushButton_0.setFlat(False)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 12, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 6, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_1.setAutoDefault(True)
        self.pushButton_1.setDefault(False)
        self.pushButton_1.setFlat(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 10, 0, 1, 1)
        self.pushButton_multiply = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_multiply.setAutoDefault(True)
        self.pushButton_multiply.setDefault(False)
        self.pushButton_multiply.setFlat(False)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.gridLayout.addWidget(self.pushButton_multiply, 7, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.text_output = QtWidgets.QTextBrowser(self.gridWidget)
        self.text_output.setMinimumSize(QtCore.QSize(0, 0))
        self.text_output.setObjectName("text_output")
        self.gridLayout.addWidget(self.text_output, 0, 0, 1, 5)
        self.pushButton_mod = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_mod.setAutoDefault(True)
        self.pushButton_mod.setDefault(False)
        self.pushButton_mod.setFlat(False)
        self.pushButton_mod.setObjectName("pushButton_mod")
        self.gridLayout.addWidget(self.pushButton_mod, 12, 2, 1, 1)
        self.text_input = QtWidgets.QLineEdit(self.gridWidget)
        self.text_input.setAutoFillBackground(False)
        self.text_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.text_input.setObjectName("text_input")
        self.gridLayout.addWidget(self.text_input, 2, 0, 1, 5)
        self.pushButton_add = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_add.setAutoDefault(True)
        self.pushButton_add.setDefault(False)
        self.pushButton_add.setFlat(False)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 12, 3, 1, 1)
        self.pushButton_exp = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_exp.setAutoDefault(True)
        self.pushButton_exp.setDefault(False)
        self.pushButton_exp.setFlat(False)
        self.pushButton_exp.setObjectName("pushButton_exp")
        self.gridLayout.addWidget(self.pushButton_exp, 12, 4, 1, 1)
        self.pushButton_brac_open = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_brac_open.setObjectName("pushButton_brac_open")
        self.gridLayout.addWidget(self.pushButton_brac_open, 6, 4, 1, 1)
        self.pushButton_brac_close = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_brac_close.setObjectName("pushButton_brac_close")
        self.gridLayout.addWidget(self.pushButton_brac_close, 7, 4, 1, 1)
        self.pushButton_root = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_root.setObjectName("pushButton_root")
        self.gridLayout.addWidget(self.pushButton_root, 10, 4, 1, 1)
        self.pushButton_equals = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_equals.setAutoDefault(True)
        self.pushButton_equals.setDefault(False)
        self.pushButton_equals.setFlat(False)
        self.pushButton_equals.setObjectName("pushButton_equals")
        self.gridLayout.addWidget(self.pushButton_equals, 4, 4, 1, 1)
        self.pushButton_ans = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_ans.setAutoDefault(True)
        self.pushButton_ans.setObjectName("pushButton_ans")
        self.gridLayout.addWidget(self.pushButton_ans, 4, 3, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_clear.setAutoDefault(True)
        self.pushButton_clear.setDefault(False)
        self.pushButton_clear.setFlat(False)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 4, 2, 1, 1)
        self.output_msg = QtWidgets.QLabel(self.gridWidget)
        self.output_msg.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.output_msg.setText("")
        self.output_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.output_msg.setObjectName("output_msg")
        self.gridLayout.addWidget(self.output_msg, 4, 0, 1, 2)
        self.gridLayout_2.addWidget(self.gridWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.text_input, self.pushButton_0)
        MainWindow.setTabOrder(self.pushButton_0, self.pushButton_1)
        MainWindow.setTabOrder(self.pushButton_1, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.pushButton_9)
        MainWindow.setTabOrder(self.pushButton_9, self.pushButton_dot)
        MainWindow.setTabOrder(self.pushButton_dot, self.pushButton_mod)
        MainWindow.setTabOrder(self.pushButton_mod, self.pushButton_add)
        MainWindow.setTabOrder(self.pushButton_add, self.pushButton_subtract)
        MainWindow.setTabOrder(self.pushButton_subtract, self.pushButton_multiply)
        MainWindow.setTabOrder(self.pushButton_multiply, self.pushButton_divide)
        MainWindow.setTabOrder(self.pushButton_divide, self.pushButton_brac_open)
        MainWindow.setTabOrder(self.pushButton_brac_open, self.pushButton_brac_close)
        MainWindow.setTabOrder(self.pushButton_brac_close, self.pushButton_root)
        MainWindow.setTabOrder(self.pushButton_root, self.pushButton_exp)
        MainWindow.setTabOrder(self.pushButton_exp, self.pushButton_equals)
        MainWindow.setTabOrder(self.pushButton_equals, self.pushButton_ans)
        MainWindow.setTabOrder(self.pushButton_ans, self.pushButton_clear)
        MainWindow.setTabOrder(self.pushButton_clear, self.text_output)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_subtract.setText(_translate("MainWindow", "-"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_multiply.setText(_translate("MainWindow", "*"))
        self.text_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_mod.setText(_translate("MainWindow", "%"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_exp.setText(_translate("MainWindow", "^"))
        self.pushButton_brac_open.setText(_translate("MainWindow", "("))
        self.pushButton_brac_close.setText(_translate("MainWindow", ")"))
        self.pushButton_root.setText(_translate("MainWindow", "√"))
        self.pushButton_equals.setText(_translate("MainWindow", "="))
        self.pushButton_ans.setText(_translate("MainWindow", "Ans"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
