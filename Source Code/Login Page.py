from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QGuiApplication
import sys


class Login(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EdVenture")
        self.showMaximized()

        
        
        

app = QApplication(sys.argv)


loginWindow = Login()
loginWindow.show()

app.exec()