from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenuBar, QWidget, 
    QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget, QLabel
)

#for now
class AddStudentDialog(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(400, 300)
        self.show()
