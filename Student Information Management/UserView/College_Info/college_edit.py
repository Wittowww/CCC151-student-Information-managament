from PySide6.QtWidgets import (
    QDialog, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QMessageBox
)
from Logics.CSV_handler import get_college, update_college

class EditCollegeDialog(QDialog):
    def __init__(self, college_code, parent=None):
        super().__init__(parent)
        self.college_code = college_code
        self.setWindowTitle("Edit College")
        self.setFixedSize(500, 200)
        self.setup_ui()
        self.load_college_data()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        college_Form = QFormLayout()

        self.collegeCode_input = QLineEdit()
        self.collegeCode_input.setReadOnly(True)  # ID cannot be changed
        self.collegeName_input = QLineEdit()

        college_Form.addRow("College Code:", self.collegeCode_input)
        college_Form.addRow("College Name:", self.collegeName_input)

        layout.addLayout(college_Form)

        self.college_saveButton = QPushButton("Save Changes")
        self.college_saveButton.clicked.connect(self.submit_edit)

        self.college_cancelButton = QPushButton("Cancel")
        self.college_cancelButton.clicked.connect(self.close)

        layout.addWidget(self.college_saveButton)
        layout.addWidget(self.college_cancelButton)

        self.setLayout(layout)

    def load_college_data(self):
        """pre fills the form with existing college data"""
        college = get_college(self.college_code)

        if college:
            self.collegeCode_input.setText(college["College Code"])
            self.collegeName_input.setText(college["College Name"])
        else:
            QMessageBox.warning(self, "Error", "College not found!")
            self.close()

    def submit_edit(self):
        updated = {
            "College Code": self.collegeCode_input.text().strip(),
            "College Name": self.collegeName_input.text().strip()
        }

        if any(v == "" for v in updated.values()):
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        result = update_college(updated)

        if result:
            QMessageBox.information(self, "Success", "College updated successfully!")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "College not found!")