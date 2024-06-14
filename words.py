from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # keeps track of the text in the box
        self.text_in_box = ""

        self.setWindowTitle("Words App")

        pagelayout = QVBoxLayout()
        textlayout = QHBoxLayout()


        # page title
        title = QLabel("Text Box and Label Box")
        pagelayout.addWidget(title)
        pagelayout.addLayout(textlayout)


        # word boxes
        self.textbox = QLineEdit()
        self.textbox.setPlaceholderText("Type something here")
        self.textbox.textChanged.connect(self.text_changed)
        self.textbox.textChanged.connect(self.change_in_other_box)
        textlayout.addWidget(self.textbox)

        # non-changeable text box
        self.unchanged_text = QLineEdit()
        self.unchanged_text.setPlaceholderText("Change the text in the other box to change the text in this box")
        self.unchanged_text.setReadOnly(True)
        textlayout.addWidget(self.unchanged_text)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
    
    def text_changed(self, text):
        # print("the text was changed")
        self.text_in_box = text
        #self.change_in_other_box
    
    def change_in_other_box(self):
        # changes the text in the right textbox when the left textbox changes
        self.unchanged_text.setPlaceholderText(self.text_in_box)

# application instance
app = QApplication(sys.argv)

# QtWidget, or the new window
window = MainWindow()
window.show() # since the window is initially hidden

# starts the event loop
app.exec()
