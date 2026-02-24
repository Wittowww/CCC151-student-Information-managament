import os

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget, QLabel, QLineEdit, QComboBox
)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt

from GUI.GUIlook import WIN98_STYLE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Dialog imports
from UserView.Student_Info.student_add import AddStudentDialog
from UserView.College_Info.college_add import AddCollegeDialog
from UserView.Program_Info.program_add import AddProgramDialog   

#Table imports
from UserView.Student_Info.view_student_table import StudentTable
from UserView.College_Info.view_college_table import CollegeTable
from UserView.Program_Info.view_program_table import ProgramTable


class mainApp(QMainWindow):

    SORT_OPTIONS = {
    0: [  # Student Table
        ("Sort by Student ID",   0),
        ("Sort by Last Name",    1),
        ("Sort by First Name",   2),
        ("Sort by Gender",       3),
        ("Sort by Program Code", 4),
        ("Sort by Year",         5),
    ],
    1: [  # College Table
        ("Sort by College Code", 0),
        ("Sort by College Name", 1),
    ],
    2: [  # Program Table
        ("Sort by Program Code", 0),
        ("Sort by Program Name", 1),
        ("Sort by College Code", 2),
    ],
}

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Information Management System")
        self.setFixedSize(1200, 700)
        
        icon_path = os.path.join(BASE_DIR, "StudentInfo ICON.png")
        self.setWindowIcon(QIcon(icon_path))

        self.setStyleSheet(WIN98_STYLE)
        
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
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.handle_search)
        self.search_bar.returnPressed.connect(self.handle_search)  # Search on Enter key too

        # Clear button to reset search
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_search)

        upperBar.addWidget(self.search_bar)
        upperBar.addWidget(self.search_button)
        upperBar.addWidget(self.clear_button)

        #Sort
        self.sort_box = QComboBox()
        self.sort_box.currentIndexChanged.connect(self.handle_sort)
        upperBar.addWidget(self.sort_box)

        self.button_students.clicked.connect(self.update_sort_options)
        self.button_colleges.clicked.connect(self.update_sort_options)
        self.button_programs.clicked.connect(self.update_sort_options)

        #ADD button (add data)
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
        self.update_sort_options()

    #for add Button, so it shows a certain dialog when a certain table is open
    def handle_add_context(self):
        index = self.stackTables.currentIndex()
        if index == 0: self.popup_addStudent()
        elif index == 1: self.popup_addCollege()
        elif index == 2: self.popup_addProgram()

    #for Search huhuhuhu
    def handle_search(self):
        query = self.search_bar.text().strip().lower()
        current_table_widget = self.stackTables.currentWidget().table

        for row in range(current_table_widget.rowCount()):
        # If query is empty, show all rows
            if not query:
                current_table_widget.setRowHidden(row, False)
                continue

            match = False
            for col in range(current_table_widget.columnCount()):  # ← inside for row
                item = current_table_widget.item(row, col)
                if item and query in item.text().lower():
                    match = True
                    break

            current_table_widget.setRowHidden(row, not match) 

    def clear_search(self):
        self.search_bar.clear()
        self.handle_search()

    def update_sort_options(self):
        index = self.stackTables.currentIndex()
        self.sort_box.blockSignals(True)  # Prevent sort from triggering while updating
        self.sort_box.clear()
        self.sort_box.addItems([label for label, _ in self.SORT_OPTIONS[index]])
        self.sort_box.blockSignals(False)

    def handle_sort(self, combo_index):
        table_index = self.stackTables.currentIndex()
        options = self.SORT_OPTIONS.get(table_index, [])

        if combo_index < 0 or combo_index >= len(options):
            return

        _, col = options[combo_index]
        current_table_widget = self.stackTables.currentWidget().table
        current_table_widget.sortItems(col, Qt.AscendingOrder)

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
