from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMenuBar, QWidget, 
    QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget, QLabel
)
from PySide6.QtGui import QIcon
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

        self.MenuBar_setup()
        self.UI_setup(central_widget)
        self.show()

    # Main Window Layout
    def UI_setup(self, central_widget):
        layout_main = QHBoxLayout(central_widget)

        #upper bar
        upperBar = QHBoxLayout()
        
        #left side bar(due to QV)
        sideBar = QVBoxLayout()


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


        # Buttons for side bar frfr
        self.button_addStudent = QPushButton("Add Student")
        self.button_addProgram = QPushButton("Add Program")
        self.button_addCollege = QPushButton("Add College")
        #buttonc actions :P
        self.button_addStudent.clicked.connect(self.popup_addStudent)
        self.button_addProgram.clicked.connect(self.popup_addProgram)
        self.button_addCollege.clicked.connect(self.popup_addCollege)
        #add button to side bar
        sideBar.addWidget(self.button_addStudent)
        sideBar.addWidget(self.button_addProgram)
        sideBar.addWidget(self.button_addCollege)
        sideBar.addStretch()


        #Right content area (for the tables/list)
        self.stackTables = QStackedWidget()

        self.stackTables.addWidget(StudentTable())
        self.stackTables.addWidget(CollegeTable())
        self.stackTables.addWidget(ProgramTable())

        layout_main.addLayout(upperBar)
        layout_main.addLayout(sideBar)
        layout_main.addWidget(self.stackTables)


    # menu Bar for Addition (may continue or not)
    def MenuBar_setup(self):
        menu_bar = self.menuBar()

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
