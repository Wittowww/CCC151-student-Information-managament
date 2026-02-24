from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget, QLabel, QLineEdit, QComboBox
)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt

#Dialog imports
from UserView.Student_Info.student_add import AddStudentDialog
from UserView.College_Info.college_add import AddCollegeDialog
from UserView.Program_Info.program_add import AddProgramDialog   

#Table imports
from UserView.Student_Info.view_student_table import StudentTable
from UserView.College_Info.view_college_table import CollegeTable
from UserView.Program_Info.view_program_table import ProgramTable


class mainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Information Management System")
        self.setFixedSize(1200, 700)
        self.setWindowIcon(QIcon("StudentInfo ICON.png"))
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.UI_setup(central_widget)
        self.show()

    # Main Window Layout
    def UI_setup(self, central_widget):
        layout_main = QVBoxLayout(central_widget)

        #upper bar
        upperBar = QHBoxLayout()
        upperBar.setSpacing(5)

        #Buttons for upper bar foreall
        self.button_students = QPushButton("Student")
        self.button_colleges = QPushButton("College")
        self.button_programs = QPushButton("Program")
        #add button to upper bar
        upperBar.addWidget(self.button_students)
        upperBar.addWidget(self.button_colleges)
        upperBar.addWidget(self.button_programs)
        #Button actions 
        self.button_students.clicked.connect(self.show_studentTable)
        self.button_colleges.clicked.connect(self.show_collegeTable)
        self.button_programs.clicked.connect(self.show_programTable)

        upperBar.addStretch()

        #Search engine? Engine?!
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setFixedWidth(200)
        self.search_bar.textChanged.connect(self.handle_search)
        upperBar.addWidget(self.search_bar)

        #Sort
        self.sort_box = QComboBox()
        self.sort_box.addItems(["Sort by ID", "Sort by Name"])
        self.sort_box.currentIndexChanged.connect(self.handle_sort)
        upperBar.addWidget(self.sort_box)

        self.button_Add = QPushButton("Add New")
        upperBar.addWidget(self.button_Add)
        self.button_Add.clicked.connect(self.handle_add_context)

        #Right content area (for the tables/list)
        self.stackTables = QStackedWidget()

        self.stackTables.addWidget(StudentTable())
        self.stackTables.addWidget(CollegeTable())
        self.stackTables.addWidget(ProgramTable())

        layout_main.addLayout(upperBar)
        layout_main.addWidget(self.stackTables)

    #for add Button, so it shows a certain dialog when a certain table is open
    def handle_add_context(self):
        index = self.stackTables.currentIndex()
        if index == 0: self.popup_addStudent()
        elif index == 1: self.popup_addCollege()
        elif index == 2: self.popup_addProgram()

    #for Search huhuhuhu
    def handle_search(self):
        query = self.search_bar.text().lower()
    # Get the QTableWidget inside the current page of the QStackedWidget
        current_table_widget = self.stackTables.currentWidget().table 

        for row in range(current_table_widget.rowCount()):
            match = False
            for col in range(current_table_widget.columnCount()):
                item = current_table_widget.item(row, col)
                if item and query in item.text().lower():
                    match = True
                    break
        current_table_widget.setRowHidden(row, not match)

    #for sort AHHH
    def handle_sort(self, index):
        current_table_widget = self.stackTables.currentWidget().table
        if index == 0:
            current_table_widget.sortItems(0, Qt.AscendingOrder)
        elif index == 1:
            current_table_widget.sortItems(1, Qt.AscendingOrder)

    #dialog functions for the add buttons
    def popup_addStudent(self):
        popup_dialog = AddStudentDialog(self)
        popup_dialog.exec()

    def popup_addCollege(self):
        popup_dialog = AddCollegeDialog(self)
        popup_dialog.exec()

    def popup_addProgram(self):
        popup_dialog = AddProgramDialog(self)
        popup_dialog.exec()

    #stack functions for the upper bar (tables)
    def show_studentTable(self):
        self.stackTables.setCurrentIndex(0)
    def show_collegeTable(self):
        self.stackTables.setCurrentIndex(1)
    def show_programTable(self):
        self.stackTables.setCurrentIndex(2)
