from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QMessageBox, QHeaderView
)
from Logics.CSV_handler import load_programs, delete_program

class ProgramTable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        btnLayout = QHBoxLayout()

        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.load_table)

        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.delete_selected)
        self.delete_btn.hide()

        self.edit_btn = QPushButton("Edit")
        self.edit_btn.clicked.connect(self.edit_selected)
        self.edit_btn.hide()

        btnLayout.addWidget(self.refresh_btn)
        btnLayout.addWidget(self.edit_btn)
        btnLayout.addWidget(self.delete_btn)
        btnLayout.addStretch()

        layout.addLayout(btnLayout)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels([
            "College Code",
            "Program Code", 
            "Program Name"
            
        ])

        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        self.table.itemClicked.connect(self.on_row_clicked)

        layout.addWidget(self.table)
        self.setLayout(layout)
        self.load_table()

    def on_row_clicked(self):
        self.delete_btn.show()
        self.edit_btn.show()

    def load_table(self):
        programs = load_programs()
        self.table.setRowCount(len(programs))
        for row_idx, program in enumerate(programs):
            self.table.setItem(row_idx, 0, QTableWidgetItem(program["College Code"]))
            self.table.setItem(row_idx, 1, QTableWidgetItem(program["Program Code"]))
            self.table.setItem(row_idx, 2, QTableWidgetItem(program["Program Name"]))

        self.delete_btn.hide()
        self.edit_btn.hide()

    def delete_selected(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a program to delete.")
            return

        program_id = self.table.item(selected_row, 1).text()

        confirm = QMessageBox.question(
            self, "Delete Program",
            f"Are you sure you want to delete <b>{program_id}<b>?<br><br>"
        )

        if confirm == QMessageBox.Yes:
            result = delete_program(program_id)
            if result:
                QMessageBox.information(self, "Success", "Program deleted!")
                self.load_table()
            else:
                QMessageBox.warning(self, "Error", "Program not found!")

    def edit_selected(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a program to edit.")
            return

        program_code = self.table.item(selected_row, 1).text()

        from UserView.Program_Info.program_edit import EditProgramDialog
        dialog = EditProgramDialog(program_code, self)
        dialog.exec()
        self.load_table()
