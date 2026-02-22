from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon


class mainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Information Management System")
        self.setGeometry(100, 100, 1200, 700)

        self.setWindowIcon(QIcon("stuinfo ICON.png"))
        self.setStyleSheet("background-color: #FFFFFF")
        
        self.show()