from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QWidget
from PySide6.QtGui import QIcon


class mainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Information Management System")
        self.setFixedSize(1200, 700)
        self.setWindowIcon(QIcon("stuinfo ICON.png"))

        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.setup_menu_bar()
        self.show()

        #menu bar and options
    def setup_menu_bar(self):
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addSeparator()
        file_menu.addAction("Exit", self.close)


        

