from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# .ui -> .py
import os
from subprocess import getstatusoutput
ui2py_flag = False
if os.path.exists("calc.ui") and getstatusoutput("pyuic5 calc.ui -o ui_calc.py")[0] == False:
    ui2py_flag = True
if ui2py_flag == False and os.path.exists("ui_calc.py") == False:
    sys.exit("No UI file") 

from processing import processing

class Window(QMainWindow, processing):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.connectSignals2Slots(self)

def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()