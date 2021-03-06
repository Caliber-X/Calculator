from PyQt5.QtCore import Qt
from ui_calc import Ui_MainWindow

root = "√"

"""
    # # # Functionalities # # #

    All Buttons                     ->      Input Text Field
    Keyboard Entry                  ->      Input Text Field
    Input Text Field                ->      Calculate Process
    Clear                           ->      Clear Text Field
    =                               ->      Moves Expression to Output Field & Ans from Down Field to Input Field
    Ans                             ->      Contains the Previous ans

"""

class processing(Ui_MainWindow):

    def __init__(self) -> None:
        super(processing,self).__init__()
        self.expression = ""
        self.ans = 0
        self._cache = ""
        self._valid = False
        # Valid Chars
        self.valid_chars = ""
        for i in range(10):
            self.valid_chars += str(i)
        self.valid_chars += ".+-*/%^()" + root
        
    def connectSignals2Slots(self, _) -> None:

        self.scrollbar = self.text_output.verticalScrollBar()

        # Text Field Changes -> Update Expression + COMPUTE
        self.text_input.textChanged[str].connect(self.compute)

        """INPUTS"""
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
        self.pushButton_root.clicked.connect    (lambda : self.update_expression(root))
        self.pushButton_exp.clicked.connect     (lambda : self.update_expression("^"))
        self.pushButton_clear.clicked.connect   (lambda : self.update_expression("cls"))
        self.pushButton_equals.clicked.connect  (self.enter_pressed)
        self.pushButton_ans.clicked.connect     (lambda : self.update_expression("ans"))

    # Update Expression on Button Click
    def update_expression(self, st) -> None:
        if st == "cls":
            self.expression = ""
        elif st == "backspace":
            self.expression = self.expression[:-1]
        elif st == "ans":
            self.expression += "ans"
        else:
            self.expression += st
        # Maintain Sync between Input_Text_Field & Expression
        self.text_input.setText(self.expression)

    # Press Enter or =
    def enter_pressed(self) -> None:
        self.ans = self.output_msg.text()
        if (not self._valid or self.output_msg.text() == ""):
            return
        cache = self.text_input.text() + " = " + str(self.ans)
        # Total cached data
        self._cache += "\n\n" + cache
        # OUTPUT Field + SCROLL BOTTOM
        self.text_output.setText(self._cache)
        self.scrollbar.setValue(self.scrollbar.maximum())
        # Change input 
        self.text_input.setText(str(self.ans))
        self.expression = str(self.ans)
        self.output_msg.clear()                 # Clear Msg Field

    # Compute on Input Field Change
    def compute(self) -> None:
        # Maintain Sync between Input_Text_Field & Expression
        self.expression = self.text_input.text()
        try:
            text = str.lower(self.text_input.text()).replace("^","**").replace("ans", str(self.ans))
            val = self.evaluate(text)
            print("{} -> {}".format(text, val))
            self.output_msg.setText(str(val))
            self._valid = True
        except:
            self.output_msg.setText("Invalid")
            self._valid = False

    # Helper evaluation function to handle security exceptions and square root functionality
    def evaluate(self, st) -> int:
        flag = 0

        # Security -> Anything undefined will not be compiled
        for char in st:
            if char not in self.valid_chars:
                flag = 1
                break
        if flag == 1:
            raise Exception

        # Square Root functionality
        if root in st:
            st = self._sq_root(st)

        return eval(st)

    # Helper function to mangle root expressions
    def _sq_root(self, st):
        # Mangles the String from √x -> x^0.5
        new_str = ""
        skip = 0
        for i in range(len(st)):
            i += skip
            if i >= len(st):
                break
            if st[i] == root:
                j = i+1
                while(st[j] in "0123456789."):
                    j+=1
                    if j >= len(st):
                        break
                replacement = "("+st[i+1:j]+"**0.5)"
                if st[i-1] in "0123456789" and i != 0:
                    replacement = "*" + replacement
                new_str += replacement
                skip += j - i - 1
            else:
                new_str += st[i]
        return new_str


    """KEY Press Event for Keys -> Button Click Map"""
    def keyPressEvent(self, event):
        
        if event.key() == Qt.Key.Key_0:
            self.pushButton_0.animateClick()

        elif event.key() == Qt.Key.Key_1:
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
        
        elif event.key() == Qt.Key.Key_A:
            self.pushButton_ans.animateClick()

        else:
            pass

