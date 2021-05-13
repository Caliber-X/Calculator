from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import calc_ui

class App(QtWidgets.QMainWindow, calc_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()