from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QMessageBox, QHeaderView
)
from Logics.CSV_handler import load_students, delete_student

class StudentTable(QWidget):
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
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Student ID", 
            "Last Name", 
            "First Name", 
            "Gender", 
            "Program", 
            "Year"
        ])

        self.table.setColumnWidth(1, 200)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.setColumnWidth(5, 50)

        self.table.itemClicked.connect(self.on_row_clicked)

        layout.addWidget(self.table)
        self.setLayout(layout)
        self.load_table()

    def on_row_clicked(self):
        self.delete_btn.show()
        self.edit_btn.show()

    def load_table(self):
        students = load_students()
        self.table.setRowCount(len(students))
        for row_idx, student in enumerate(students):
            self.table.setItem(row_idx, 0, QTableWidgetItem(student["Student ID"]))
            self.table.setItem(row_idx, 1, QTableWidgetItem(student["First Name"]))
            self.table.setItem(row_idx, 2, QTableWidgetItem(student["Last Name"]))
            self.table.setItem(row_idx, 3, QTableWidgetItem(student["Gender"]))
            self.table.setItem(row_idx, 4, QTableWidgetItem(student["Program Code"]))
            self.table.setItem(row_idx, 5, QTableWidgetItem(student["Year"]))

        self.delete_btn.hide()
        self.edit_btn.hide()

    def delete_selected(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a student to delete.")
            return

        student_id = self.table.item(selected_row, 0).text()

        confirm = QMessageBox.question(
            self, "Delete Student",
            f"Are you sure you want to delete <b>{student_id}<b>?<br><br>"
        )

        if confirm == QMessageBox.Yes:
            result = delete_student(student_id)
            if result:
                QMessageBox.information(self, "Success", "Student deleted!")
                self.load_table()
            else:
                QMessageBox.warning(self, "Error", "Student not found!")

    def edit_selected(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a student to edit.")
            return

        student_id = self.table.item(selected_row, 0).text()

        from UserView.Student_Info.student_edit import EditStudentDialog
        dialog = EditStudentDialog(student_id, self)
        dialog.exec()
        self.load_table()