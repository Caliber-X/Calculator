from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

# Pre-compile UI file
import os
os.system("pyuic5 calc.ui -o ui_calc.py")
import ui_calc

class UI(QtWidgets.QMainWindow, ui_calc.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = UI()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()