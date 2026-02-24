from PySide6.QtWidgets import (
    QDialog, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QMessageBox, QComboBox
)
from Logics.CSV_handler import get_student, update_student, load_programs, load_colleges

class EditStudentDialog(QDialog):
    def __init__(self, student_id, parent=None):
        super().__init__(parent)
        self.student_id = student_id
        self.setWindowTitle("Edit Student")
        self.setFixedSize(500, 300)
        self.setup_ui()
        self.load_student_data()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        student_Form = QFormLayout()

        self.studentID_input = QLineEdit()
        self.studentID_input.setReadOnly(True)  # ID cannot be changed
        self.studentFirstName_input = QLineEdit()
        self.studentLastName_input = QLineEdit()
        self.studentYear_input = QLineEdit()

        #Gender Drop Down
        self.studentGender_input = QComboBox()
        self.studentGender_input.addItems(["Select Gender", "Female", "Male"])

        #drop down for college
        self.college_input = QComboBox()
        self.load_colleges()
        self.college_input.currentIndexChanged.connect(self.filter_programs)

        # program dropdown
        self.program_input = QComboBox()
        self.load_programs()

        student_Form.addRow("Student ID:", self.studentID_input)
        student_Form.addRow("First Name:", self.studentFirstName_input)
        student_Form.addRow("Last Name:", self.studentLastName_input)
        student_Form.addRow("Gender:", self.studentGender_input)
        student_Form.addRow("Year:", self.studentYear_input)
        student_Form.addRow("College:", self.college_input)
        student_Form.addRow("Program:", self.program_input)
        

        layout.addLayout(student_Form)

        self.student_saveButton = QPushButton("Save Changes")
        self.student_saveButton.clicked.connect(self.submit_edit)

        self.student_cancelButton = QPushButton("Cancel")
        self.student_cancelButton.clicked.connect(self.close)

        layout.addWidget(self.student_saveButton)
        layout.addWidget(self.student_cancelButton)

        self.setLayout(layout)

    def load_colleges(self):
        colleges = load_colleges()
        self.college_input.clear()
        self.college_input.addItem("Select College", "Select College")
        for college in colleges:
            self.college_input.addItem(
                f"{college['College Code']} - {college['College Name']}",
                college["College Code"]
            )

    def filter_programs(self):
        selected_college_code = self.college_input.currentData()
        programs = load_programs()

        self.program_input.clear()

        if not selected_college_code:
            self.program_input.addItem("Select College first", "")
            return

        filtered = [p for p in programs if p["College Code"] == selected_college_code]

        if not filtered:
            self.program_input.addItem("No programs found", "Select Program")
            return

        self.program_input.addItem("Select Program", "")
        for program in filtered:
            self.program_input.addItem(
                f"{program['Program Code']} - {program['Program Name']}",
                program["Program Code"]
            )

    def load_programs(self):
        programs = load_programs()
        self.program_input.clear()
        self.program_input.addItem("Program", "") 
        for program in programs:
            self.program_input.addItem(
                program["Program Name"], 
                program["Program Code"]
            )

    def load_student_data(self):
        student = get_student(self.student_id)

        if student:
            self.studentID_input.setText(student["Student ID"])
            self.studentFirstName_input.setText(student["First Name"])
            self.studentLastName_input.setText(student["Last Name"])
            self.studentGender_input.setCurrentText(student["Gender"])
            self.studentYear_input.setText(student["Year"])

            
            index = self.program_input.findData(student["Program Code"])
            if index >= 0:
                self.program_input.setCurrentIndex(index)
        else:
            QMessageBox.warning(self, "Error", "Student not found!")
            self.close()

    def submit_edit(self):
        updated = {
            "Student ID": self.studentID_input.text().strip(),
            "First Name": self.studentFirstName_input.text().strip(),
            "Last Name": self.studentLastName_input.text().strip(),
            "Gender": self.studentGender_input.currentText(),
            "Year": self.studentYear_input.text().strip(),
            "Program Code":self.program_input.currentData(),
        }

        if self.studentGender_input.currentText() == "Select Gender":
            QMessageBox.warning(self, "Input Error", "Please select a valid Gender.")
            return
        
        if self.program_input.currentData() == "Select Program":
            QMessageBox.warning(self, "Input Error", "Please select a Program.")
            return

        if any(v.strip() == "" for v in list(updated.values())[:-1]):
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        result = update_student(updated)

        if result:
            QMessageBox.information(self, "Success", "Student updated successfully!")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Student not found!")