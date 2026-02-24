from PySide6.QtWidgets import (
    QDialog, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QMessageBox
)
from Logics.CSV_handler import add_college

class AddCollegeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add College")
        self.setFixedSize(500, 300)
        self.setup_ui()
        self.show()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        college_Form = QFormLayout()

        self.collegeCode_input = QLineEdit()
        self.collegeName_input = QLineEdit()

        #input Boxes
        college_Form.addRow("College Code:", self.collegeCode_input)
        college_Form.addRow("College Name:", self.collegeName_input)

        layout.addLayout(college_Form)

        # Add and Cancel Buttons
        self.college_addButton = QPushButton("Add College")
        self.college_addButton.clicked.connect(self.submit_college)

        self.college_cancelButton = QPushButton("Cancel")
        self.college_cancelButton.clicked.connect(self.close)

        layout.addWidget(self.college_addButton)
        layout.addWidget(self.college_cancelButton)

        self.setLayout(layout)

    def submit_college(self):
        college = {
            "College Code": self.collegeCode_input.text().strip(),
            "College Name": self.collegeName_input.text().strip()
        }

        if any(v == "" for v in college.values()):         
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        add_college(college)
        QMessageBox.information(self, "Success", "College added successfully!")
        self.clear_inputs()
        self.close()

    def clear_inputs(self):
        self.collegeCode_input.clear()
        self.collegeName_input.clear()