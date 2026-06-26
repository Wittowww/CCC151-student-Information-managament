from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QMessageBox, QHeaderView
)
from PySide6.QtCore import Signal
from Logics.CSV_handler import load_colleges, delete_college
from Logics.AppSignals import app_signals  

class CollegeTable(QWidget):
    college_deleted = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        app_signals.data_changed.connect(self.load_table)

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # top buttons
        btnLayout = QHBoxLayout()

        # delete and edit buttons — hidden by default
        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.delete_selected)
        self.delete_btn.hide()

        self.edit_btn = QPushButton("Edit")
        self.edit_btn.clicked.connect(self.edit_selected)
        self.edit_btn.hide()

        btnLayout.addWidget(self.edit_btn)
        btnLayout.addWidget(self.delete_btn)
        btnLayout.addStretch()

        layout.addLayout(btnLayout)

        # table
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels([
            "College Code", 
            "College Name"
        ])

        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        self.table.itemClicked.connect(self.on_row_clicked)

        layout.addWidget(self.table)
        self.setLayout(layout)
        self.load_table()

    def on_row_clicked(self):
        self.delete_btn.show() 
        self.edit_btn.show()    

    def load_table(self):
        print("load_table called!") 
        colleges = load_colleges()
        print(f"Found {len(colleges)} colleges") 
        self.table.setRowCount(len(colleges))
        for row_idx, college in enumerate(colleges):
            self.table.setItem(row_idx, 0, QTableWidgetItem(college["College Code"]))
            self.table.setItem(row_idx, 1, QTableWidgetItem(college["College Name"]))

        self.delete_btn.hide()
        self.edit_btn.hide()

    def delete_selected(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a college to delete.")
            return

        college_code = self.table.item(selected_row, 0).text()

        confirm = QMessageBox.question(
            self, "Delete College", 
            f"Are you sure you want to delete <b>{college_code}</b>?<br><br>"
            "<b>Warning:</b> Deleting this College will result to <b>Deleted Programs</b> under it."
        )

        if confirm == QMessageBox.Yes:
            result = delete_college(college_code)
            if result:
                QMessageBox.information(self, "Success", "College deleted!")
                self.load_table()
                self.college_deleted.emit()
                app_signals.data_changed.emit() 
            else:
                QMessageBox.warning(self, "Error", "College not found!")

    def edit_selected(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a college to edit.")
            return

        college_code = self.table.item(selected_row, 0).text()

        from UserView.College_Info.college_edit import EditCollegeDialog
        dialog = EditCollegeDialog(college_code, self)
        dialog.college_updated.connect(self.load_table)
        dialog.exec()