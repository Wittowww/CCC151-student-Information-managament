from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenuBar, QWidget, 
    QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget, QLabel
)
from Logics.CSV_handler import load_students

class StudentTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.show()

