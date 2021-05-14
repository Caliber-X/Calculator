from ui_calc import Ui_MainWindow
import functools

"""
    Functionalities to implement

    Input Text Field                ->      Calculate Process
    All Buttons, Keyboard Entry     ->      Input Text Field
    Clear                           ->      Clear Text Field
    =                               ->      Moves Expression to Output Field & Ans from Down Field to Input Field
    Ans                             ->      Contains the Previous ans

"""

class processing(Ui_MainWindow):

    def __init__(self) -> None:
        super(processing,self).__init__()
        self.expression = ""

    def connectSignals2Slots(self, _):
        
        self.pushButton_clear.clicked.connect(self.text_input.clear)
        self.text_input.returnPressed.connect(self.pushButton_equals.animateClick)
        self.text_input.returnPressed.connect(self.pushButton_equals.click)
        self.text_input.textChanged[str].connect(self.compute)

        self.pushButton_0.clicked.connect(lambda : self.update_expression("0"))
        self.pushButton_1.clicked.connect(lambda : self.update_expression("1"))
        self.pushButton_2.clicked.connect(lambda : self.update_expression("2"))
        self.pushButton_3.clicked.connect(lambda : self.update_expression("3"))
        self.pushButton_4.clicked.connect(lambda : self.update_expression("4"))
        self.pushButton_5.clicked.connect(lambda : self.update_expression("5"))
        self.pushButton_6.clicked.connect(lambda : self.update_expression("6"))
        self.pushButton_7.clicked.connect(lambda : self.update_expression("7"))
        self.pushButton_8.clicked.connect(lambda : self.update_expression("8"))
        self.pushButton_9.clicked.connect(lambda : self.update_expression("9"))
        self.pushButton_dot.clicked.connect(lambda : self.update_expression("."))
        self.pushButton_add.clicked.connect(lambda : self.update_expression("+"))
        self.pushButton_subtract.clicked.connect(lambda : self.update_expression("-"))
        self.pushButton_multiply.clicked.connect(lambda : self.update_expression("*"))
        self.pushButton_divide.clicked.connect(lambda : self.update_expression("/"))
        self.pushButton_mod.clicked.connect(lambda : self.update_expression("%"))
        self.pushButton_clear.clicked.connect(lambda : self.update_expression("cls"))


    def update_expression(self, st):
        self.expression += st
        if st == "cls":
            self.expression = ""    
        self.text_input.setText(self.expression)

    def compute(self):
        print(self.text_input.text())
        # if self.text_input.text() == None:
        #     self.output_msg.setText("No Change")
        # else:
        #     self.output_msg.setText("Change")