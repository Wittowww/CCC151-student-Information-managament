from PySide6.QtWidgets import (
    QDialog, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QMessageBox, QComboBox
)
from Logics.CSV_handler import add_program, load_colleges

class AddProgramDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Program")
        self.setFixedSize(500, 300)
        self.setup_ui()
        self.show()

    def setup_ui(self):
        layout = QVBoxLayout()

        program_Form = QFormLayout()

        self.programCode_input = QLineEdit()
        self.programName_input = QLineEdit()

        #Drop Down Box for College (already has all the added colleges)
        self.college_input = QComboBox()
        self.load_colleges()

        program_Form.addRow("Program Code:", self.programCode_input)
        program_Form.addRow("Program Name:", self.programName_input)
        program_Form.addRow("College:", self.college_input)

        layout.addLayout(program_Form)

        self.program_addButton = QPushButton("Add Program")
        self.program_addButton.clicked.connect(self.submit_program)

        self.program_cancelButton = QPushButton("Cancel")
        self.program_cancelButton.clicked.connect(self.close)

        layout.addWidget(self.program_addButton) 
        layout.addWidget(self.program_cancelButton)

        self.setLayout(layout)

    def load_colleges(self):
        colleges = load_colleges()
        self.college_input.clear()
        self.college_input.addItem("Select College", "Select College")
        for college in colleges:
            self.college_input.addItem(
                college["College Name"],
                college["College Code"]
            )

    def submit_program(self):
        program = {
            "Program Code": self.programCode_input.text().strip(),
            "Program Name": self.programName_input.text().strip(),
            "College Code": self.college_input.currentData()
        }

        if any(v == "" for v in list(program.values())[:-1]):
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        add_program(program)
        QMessageBox.information(self, "Success", "Program added successfully!")
        self.clear_inputs()
        self.close()

    def clear_inputs(self):
        self.programCode_input.clear()
        self.programName_input.clear()
        self.college_input.setCurrentIndex(0)

