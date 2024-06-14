from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        pagelayout = QVBoxLayout()
        checkboxlayout = QVBoxLayout()

        # pagelayout.addLayout(checkboxlayout)


        self.setWindowTitle("My Checkbox App")

        # question
        label = QLabel("What sports do you like?")
        pagelayout.addWidget(label)

        checkbox = QCheckBox("Basketball")
        checkbox.setCheckState(Qt.CheckState.Unchecked)
        checkboxlayout.addWidget(checkbox)

        checkbox2 = QCheckBox("Football")
        checkbox2.setCheckState(Qt.CheckState.Unchecked)
        checkboxlayout.addWidget(checkbox2)

        checkbox3 = QCheckBox("Soccer")
        checkbox3.setCheckState(Qt.CheckState.Unchecked)
        checkboxlayout.addWidget(checkbox3)

        checkbox4 = QCheckBox("Other")
        checkbox4.setCheckState(Qt.CheckState.Unchecked)
        checkboxlayout.addWidget(checkbox4)


        checkbox.stateChanged.connect(self.is_checked)
        checkbox2.stateChanged.connect(self.is_checked)
        checkbox3.stateChanged.connect(self.is_checked)
        checkbox4.stateChanged.connect(self.is_checked)

        pagelayout.addLayout(checkboxlayout)
        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
    
    def is_checked(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)
    
# application instance
app = QApplication(sys.argv)

# QtWidget, or the new window
window = MainWindow()
window.show() # since the window is initially hidden

# starts the event loop
app.exec()