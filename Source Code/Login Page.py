from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys


class Login(QMainWindow): # Class for the main Login window
    def __init__(self):

        super().__init__()

        self.setWindowTitle("EdVenture") # Adds window title to EdVenture

        windowIcon = QIcon("Images\logo.png") # Defines icon 
        self.setWindowIcon(windowIcon) # Sets window icon to the logo

        #Creating the logo Image

        logoLabel = QLabel(self)
        logo = QPixmap("Images\logo.png")
        logoLabel.setPixmap(logo)

        #Creating the username and password input

        usernameInput = QLineEdit("Enter Username")
        passwordInput = QLineEdit("Enter Password")
        
        #Setting up the Layout of the login window

        emptySpace = QLabel("‎")

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

        self.showMaximized() # Makes window fullscreen


app = QApplication(sys.argv)


loginWindow = Login() # Sets window to the login window class
loginWindow.show() # Shows login window

app.exec()
