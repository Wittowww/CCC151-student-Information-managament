from PySide6.QtWidgets import (
    QDialog, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QMessageBox, QComboBox
)
from Logics.CSV_handler import get_student, update_student, load_programs

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
        self.studentGender_input = QLineEdit()
        self.studentYear_input = QLineEdit()

        # program dropdown
        self.program_input = QComboBox()
        self.load_programs()

        student_Form.addRow("Student ID:", self.studentID_input)
        student_Form.addRow("First Name:", self.studentFirstName_input)
        student_Form.addRow("Last Name:", self.studentLastName_input)
        student_Form.addRow("Gender:", self.studentGender_input)
        student_Form.addRow("Program:", self.program_input)
        student_Form.addRow("Year:", self.studentYear_input)
        

        layout.addLayout(student_Form)

        self.student_saveButton = QPushButton("Save Changes")
        self.student_saveButton.clicked.connect(self.submit_edit)

        self.student_cancelButton = QPushButton("Cancel")
        self.student_cancelButton.clicked.connect(self.close)

        layout.addWidget(self.student_saveButton)
        layout.addWidget(self.student_cancelButton)

        self.setLayout(layout)

    def load_programs(self):
        """loads all programs into the dropdown"""
        programs = load_programs()
        self.program_input.clear()
        self.program_input.addItem("N/A", "N/A")  # default option
        for program in programs:
            self.program_input.addItem(
                program["Program Name"],   # text shown
                program["Program Code"]      # value stored
            )

    def load_student_data(self):
        """pre fills the form with existing student data"""
        student = get_student(self.student_id)

        if student:
            self.studentID_input.setText(student["Student ID"])
            self.studentFirstName_input.setText(student["First Name"])
            self.studentLastName_input.setText(student["Last Name"])
            self.studentGender_input.setText(student["Gender"])
            self.studentYear_input.setText(student["Year"])

            # set dropdown to current program
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
            "Gender": self.studentGender_input.text().strip(),
            "Year": self.studentYear_input.text().strip(),
            "Program":self.program_input.currentData(),
        }

        if any(v.strip() == "" for v in list(updated.values())[:-1]):
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        result = update_student(updated)

        if result:
            QMessageBox.information(self, "Success", "Student updated successfully!")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Student not found!")