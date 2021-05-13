import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

class main():
    def __init__(self):
        # 3. Create an instance of your application's GUI
        self.window = QWidget()
        self.window.setWindowTitle("PyQt5 App")
        self.window.setGeometry(100, 100, 280, 80)
        self.window.move(60, 15)
        self.helloMsg = QLabel("<h1>Hello World</h1>", parent=self.window)
        self.helloMsg.move(60, 15)

        # 4. Show your application's GUI
        self.window.show()

obj = main()

# # 3. Create an instance of your application's GUI
# window = QWidget()
# window.setWindowTitle("PyQt5 App")
# window.setGeometry(100, 100, 280, 80)
# window.move(60, 15)
# helloMsg = QLabel("<h1>Hello World</h1>", parent=window)
# helloMsg.move(60, 15)

# # 4. Show your application's GUI
# window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())
