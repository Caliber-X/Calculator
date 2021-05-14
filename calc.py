from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys

# # .ui -> .py
# import os
# from subprocess import getstatusoutput
# ui2py_flag = False
# if os.path.exists("calc.ui") and getstatusoutput("pyuic5 calc.ui -o ui_calc.py")[0] == False:
#     ui2py_flag = True
# if ui2py_flag == False and os.path.exists("ui_calc.py") == False:
#     sys.exit("No UI file") 
# from ui_calc import Ui_MainWindow

# class UI(QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(UI, self).__init__(parent)
#         self.setupUi(self)

# Load UI from .ui file directly
class UI(QMainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        uic.loadUi("calc.ui", self)

def main():
    app = QApplication(sys.argv)
    win = UI()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()