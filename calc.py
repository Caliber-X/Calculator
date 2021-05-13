from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

# .ui -> .py
import os
if os.path.exists("calc.ui"):
    os.system("pyuic5 calc.ui -o ui_calc.py")
elif os.path.exists("ui_calc.py") == False:
    sys.exit("No UI file") 
import ui_calc

class UI(QtWidgets.QMainWindow, ui_calc.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    win = UI()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()