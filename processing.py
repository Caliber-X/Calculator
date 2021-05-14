from ui_calc import Ui_MainWindow

class processing(Ui_MainWindow):
    def connectSignals2Slots(self, _):
        
        self.pushButton_clear.clicked.connect(self.text_input.clear)
        self.text_input.returnPressed.connect(self.pushButton_equals.animateClick)
        self.text_input.returnPressed.connect(self.pushButton_equals.click)