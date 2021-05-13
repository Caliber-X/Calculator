import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("GRID")

layout = QGridLayout()
# layout.addWidget(QLineEdit().setReadOnly(True), 0, 0, 1, 3)
# layout.addWidget(QLineEdit(), 1, 0, 1, 3)

for i in range (0, 3):
    for j in range (0, 3):
        layout.addWidget(QPushButton(str(3*i+j)), i+2, j)


window.setLayout(layout)
window.show()

sys.exit(app.exec_())