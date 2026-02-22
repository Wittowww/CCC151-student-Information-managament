from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QWidget
from PySide6.QtGui import QIcon


class mainApp(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Student Information Management System")
        self.setFixedSize(1200, 700)
        self.setWindowIcon(QIcon("stuinfo ICON.png"))
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.setup_menu_bar()
        #self.GUI_style()
        self.show()

        #menu bar and options
    def setup_menu_bar(self):
        menu_bar = self.menuBar()

        

