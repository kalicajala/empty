# imports
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt
import sys

# subclass for main window
class MainWindow(QMainWindow):
    # will run when main window object is created
    def __init__(self):
        # number tracker
        self.numClicks = 0
        # since MainWindow is a subclass of QMainWindow
        # lets MainWindow implement constructor of QMainWindow
        super().__init__()

        # titles the window
        self.setWindowTitle("My Button Application")

        # adds and titles a button on the window
        button = QPushButton("Push me")
        button.setCheckable(True) # checks if the button was pressed. if so, it will run the following function
        button.clicked.connect(self.button_was_clicked) # method on the window
        button.clicked.connect(self.button_is_blue) # another method onthe window
        button.clicked.connect(self.increase_click_count) # another method on the window

        # centers the button to the middle fo the window
        self.setCentralWidget(button)

    def button_was_clicked(self):
        print("The button was clicked")
    
    def button_is_blue(self, blue):
        print("The button is blue?", blue)
    
    def increase_click_count(self, currNumber):
        self.numClicks += 1
        print("Number of times the button was clicked: ", self.numClicks)

# application instance
app = QApplication(sys.argv)

# QtWidget, or the new window
window = MainWindow()
window.show() # since the window is initially hidden

# starts the event loop
app.exec()
