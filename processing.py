from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from ui_calc import Ui_MainWindow

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
        self.ans = 0
        
    def connectSignals2Slots(self, _) -> None:

        # COMPUTE <- Text Field Changes
        self.text_input.textChanged[str].connect(self.compute)

        """INPUTS"""

        # Change Input Field Directly
        self.expression = self.text_input.text()

        # Buttons Click -> Form Expression
        self.pushButton_0.clicked.connect       (lambda : self.update_expression("0"))
        self.pushButton_1.clicked.connect       (lambda : self.update_expression("1"))
        self.pushButton_2.clicked.connect       (lambda : self.update_expression("2"))
        self.pushButton_3.clicked.connect       (lambda : self.update_expression("3"))
        self.pushButton_4.clicked.connect       (lambda : self.update_expression("4"))
        self.pushButton_5.clicked.connect       (lambda : self.update_expression("5"))
        self.pushButton_6.clicked.connect       (lambda : self.update_expression("6"))
        self.pushButton_7.clicked.connect       (lambda : self.update_expression("7"))
        self.pushButton_8.clicked.connect       (lambda : self.update_expression("8"))
        self.pushButton_9.clicked.connect       (lambda : self.update_expression("9"))
        self.pushButton_dot.clicked.connect     (lambda : self.update_expression("."))
        self.pushButton_add.clicked.connect     (lambda : self.update_expression("+"))
        self.pushButton_subtract.clicked.connect(lambda : self.update_expression("-"))
        self.pushButton_multiply.clicked.connect(lambda : self.update_expression("*"))
        self.pushButton_divide.clicked.connect  (lambda : self.update_expression("/"))
        self.pushButton_mod.clicked.connect     (lambda : self.update_expression("%"))
        self.pushButton_brac_open.clicked.connect(lambda : self.update_expression("("))
        self.pushButton_brac_close.clicked.connect(lambda : self.update_expression(")"))
        self.pushButton_root.clicked.connect    (lambda : self.update_expression("√"))
        self.pushButton_exp.clicked.connect     (lambda : self.update_expression("^"))
        self.pushButton_clear.clicked.connect   (lambda : self.update_expression("cls"))
        self.pushButton_equals.clicked.connect  (self.move2_output_field)
        

    def update_expression(self, st) -> None:
        if st == "cls":
            self.expression = ""
        elif st == "backspace":
            self.expression = self.expression[:-1]
        else:
            self.expression += st
        self.text_input.setText(self.expression)

    def compute(self) -> None:
        try:
            val = eval(self.text_input.text().replace("^","**"))
            print(val)
            self.output_msg.setText(str(val))
            self.ans = val
        except:
            self.output_msg.setText("Invalid")

    def move2_output_field(self) -> None:
        print("ENTER Pressed")



    """KEY Press Event for Keys -> Button Click Map"""
    def keyPressEvent(self, event):
        
        if event.key() == Qt.Key.Key_1:
            self.pushButton_1.animateClick()

        elif event.key() == Qt.Key.Key_2:
            self.pushButton_2.animateClick()

        elif event.key() == Qt.Key.Key_3:
            self.pushButton_3.animateClick()

        elif event.key() == Qt.Key.Key_4:
            self.pushButton_4.animateClick()

        elif event.key() == Qt.Key.Key_5:
            self.pushButton_5.animateClick()

        elif event.key() == Qt.Key.Key_6:
            self.pushButton_6.animateClick()

        elif event.key() == Qt.Key.Key_7:
            self.pushButton_7.animateClick()

        elif event.key() == Qt.Key.Key_8:
            self.pushButton_8.animateClick()
        
        elif event.key() == Qt.Key.Key_9:
            self.pushButton_9.animateClick()

        elif event.key() == Qt.Key.Key_Period:
            self.pushButton_dot.animateClick()

        elif event.key() == Qt.Key.Key_Plus:
            self.pushButton_add.animateClick()

        elif event.key() == Qt.Key.Key_Minus:
            self.pushButton_subtract.animateClick()

        elif event.key() == Qt.Key.Key_Asterisk:
            self.pushButton_multiply.animateClick()

        elif event.key() == Qt.Key.Key_Slash:
            self.pushButton_divide.animateClick()

        elif event.key() == Qt.Key.Key_ParenLeft:
            self.pushButton_brac_open.animateClick()

        elif event.key() == Qt.Key.Key_ParenRight:
            self.pushButton_brac_close.animateClick()

        elif event.key() == Qt.Key.Key_AsciiCircum:
            self.pushButton_exp.animateClick()

        elif event.key() == Qt.Key.Key_Backspace:
            self.update_expression("backspace")

        elif event.key() == Qt.Key.Key_Escape:
            self.pushButton_clear.animateClick()

        elif event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            self.pushButton_equals.animateClick()
        
        else:
            pass

