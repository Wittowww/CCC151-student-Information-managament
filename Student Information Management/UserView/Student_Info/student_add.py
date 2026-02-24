from PySide6.QtWidgets import (
    QDialog, QLineEdit, QVBoxLayout, QPushButton, QFormLayout, QLabel, QMessageBox, QComboBox
)

from Logics.CSV_handler import add_student, load_programs

#for now
class AddStudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Student")
        self.setFixedSize(500, 300)
        self.setup_ui()
        self.show()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        student_Form = QFormLayout()

        self.studentID_input = QLineEdit()
        self.studentFirstName_input = QLineEdit()
        self.studentLastName_input = QLineEdit()
        self.studentYear_input = QLineEdit()

        self.studentGender_input = QComboBox()
        self.studentGender_input.addItems(["Select Gender", "Female", "Male"])

        #Drop Down Box for Program (already has all the added programs)
        self.program_input = QComboBox()
        self.load_Programs()

        #Input Boxes
        student_Form.addRow("Student ID:", self.studentID_input)
        student_Form.addRow("First Name:", self.studentFirstName_input)
        student_Form.addRow("Last Name:", self.studentLastName_input)
        student_Form.addRow("Gender:", self.studentGender_input)
        student_Form.addRow("Year:", self.studentYear_input)
        student_Form.addRow("Program:", self.program_input)

        layout.addLayout(student_Form)

        #Add and Cancel Buttons
        self.student_addButton = QPushButton("Add Student")
        self.student_addButton.clicked.connect(self.submit_student)

        self.student_cancelButton = QPushButton("Cancel")
        self.student_cancelButton.clicked.connect(self.close)

        layout.addWidget(self.student_addButton)
        layout.addWidget(self.student_cancelButton)

        self.setLayout(layout)

    def load_Programs(self):
        programs = load_programs()
        self.program_input.clear()
        self.program_input.addItem("N/A", "N/A")
        for program in programs:
            self.program_input.addItem(
                program["Program Name"],
                program["Program Code"]
            )

    def submit_student(self):
        students = {
            "Student ID": self.studentID_input.text().strip(),
            "First Name": self.studentFirstName_input.text().strip(),
            "Last Name": self.studentLastName_input.text().strip(),
            "Gender": self.studentGender_input.currentData(),
            "Year": self.studentYear_input.text().strip(),
            "Program": self.program_input.currentData()
        }

        if any (v == "" for v in list(students.values())[:-1]):
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        add_student(students)
        QMessageBox.information(self, "Success", "Student added successfully!")
        self.clear_inputs()
        self.close()

    def clear_inputs(self):
            self.studentID_input.clear()
            self.studentFirstName_input.clear()
            self.studentLastName_input.clear()
            self.studentGender_input.clear()
            self.studentYear_input.clear()
            self.program_input.setCurrentIndex(0)

