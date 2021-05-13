import sys
from PyQt5.QtCore import left

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QLabel

app = QApplication(sys.argv)

# Main window properties
window = QWidget()
window.setWindowTitle("Horizontal Stack")
layout = QHBoxLayout()
window.setWindowTitle("Vertical Stack")
layout = QVBoxLayout()

# window.setGeometry(0, 0, 0, 0)

# Layout
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))

# Add layout to window
window.setLayout(layout)

window.show()

sys.exit(app.exec_())
