import sys

from PyQt5.QtWidgets import QApplication, QFormLayout, QLabel, QLineEdit, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("FORM")

layout = QFormLayout()
layout.addRow(QLabel("Name"), QLineEdit())

window.setLayout(layout)
window.show()
sys.exit(app.exec_())