from PySide6.QtWidgets import (
    QDialog, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QMessageBox, QComboBox
)
from Logics.CSV_handler import get_program, update_program, load_colleges

class EditProgramDialog(QDialog):
    def __init__(self, program_id, parent=None):
        super().__init__(parent)
        self.program_id = program_id
        self.setWindowTitle("Edit Program")
        self.setFixedSize(500, 600)
        self.setup_ui()
        self.load_program_data()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        program_Form = QFormLayout()

        self.programCode_input = QLineEdit()
        self.programCode_input.setReadOnly(True)  # ID cannot be changed
        self.programName_input = QLineEdit()

        # college dropdown
        self.college_input = QComboBox()
        self.load_colleges()

        program_Form.addRow("Program ID:", self.programCode_input)
        program_Form.addRow("Program Name:", self.programName_input)
        program_Form.addRow("College:", self.college_input)

        layout.addLayout(program_Form)

        self.program_saveButton = QPushButton("Save Changes")
        self.program_saveButton.clicked.connect(self.submit_edit)

        self.student_cancelButton = QPushButton("Cancel")
        self.student_cancelButton.clicked.connect(self.close)

        layout.addWidget(self.program_saveButton)
        layout.addWidget(self.student_cancelButton)

        self.setLayout(layout)

    def load_colleges(self):
        """loads all colleges into the dropdown"""
        colleges = load_colleges()
        self.college_input.clear()
        for college in colleges:
            self.college_input.addItem(
                college["College Name"],   # text shown
                college["College Code"]    # value stored
            )

    def load_program_data(self):
        """pre fills the form with existing program data"""
        program = get_program(self.program_id)

        if program:
            self.programCode_input.setText(program["Program Code"])
            self.programName_input.setText(program["Program Name"])

            # set dropdown to current college
            index = self.college_input.findData(program["College Code"])
            if index >= 0:
                self.college_input.setCurrentIndex(index)
        else:
            QMessageBox.warning(self, "Error", "Program not found!")
            self.close()

    def submit_edit(self):
        updated = {
            "Program Code": self.programCode_input.text().strip(),
            "Program Name": self.programName_input.text().strip(),
            "College Code": self.college_input.currentData()
        }

        if any(v == "" for v in updated.values()):
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        result = update_program(updated)

        if result:
            QMessageBox.information(self, "Success", "Program updated successfully!")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Program not found!")