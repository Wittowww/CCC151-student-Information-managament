
WIN98_STYLE = """
    /* Main Window */
    QMainWindow {
        background-color: #d4d0c8;
    }

    QWidget {
        background-color: #d4d0c8;
        font-family: "MS Sans Serif", Tahoma, Arial;
        font-size: 11px;
        color: #000000;
    }

    /* Buttons */
    QPushButton {
        background-color: #d4d0c8;
        border-top: 2px solid #ffffff;
        border-left: 2px solid #ffffff;
        border-right: 2px solid #808080;
        border-bottom: 2px solid #808080;
        padding: 3px 10px;
        font-family: "MS Sans Serif", Tahoma;
        font-size: 11px;
        min-width: 70px;
        min-height: 22px;
    }

    QPushButton:pressed {
        border-top: 2px solid #808080;
        border-left: 2px solid #808080;
        border-right: 2px solid #ffffff;
        border-bottom: 2px solid #ffffff;
        padding-top: 5px;
        padding-left: 12px;
    }

    QPushButton:hover {
        background-color: #d4d0c8;
    }

    /* Active/selected tab-like buttons */
    QPushButton#activeTable {
        border-top: 2px solid #808080;
        border-left: 2px solid #808080;
        border-right: 2px solid #ffffff;
        border-bottom: 2px solid #ffffff;
        background-color: #d4d0c8;
        font-weight: bold;
    }

    /* Search bar / Line Edit */
    QLineEdit {
        background-color: #ffffff;
        border-top: 2px solid #808080;
        border-left: 2px solid #808080;
        border-right: 2px solid #ffffff;
        border-bottom: 2px solid #ffffff;
        padding: 2px 4px;
        font-family: "MS Sans Serif", Tahoma;
        font-size: 11px;
        min-height: 20px;
    }

    /* ComboBox */
    QComboBox {
        background-color: #d4d0c8;
        border-top: 2px solid #ffffff;
        border-left: 2px solid #ffffff;
        border-right: 2px solid #808080;
        border-bottom: 2px solid #808080;
        padding: 2px 4px;
        font-family: "MS Sans Serif", Tahoma;
        font-size: 11px;
        min-height: 22px;
    }

    QComboBox::drop-down {
        border-left: 2px solid #808080;
        background-color: #d4d0c8;
        width: 16px;
    }

    QComboBox QAbstractItemView {
        background-color: #ffffff;
        border: 1px solid #808080;
        selection-background-color: #000080;
        selection-color: #ffffff;
    }

    /* Table */
    QTableWidget {
        background-color: #ffffff;
        border-top: 2px solid #808080;
        border-left: 2px solid #808080;
        border-right: 2px solid #ffffff;
        border-bottom: 2px solid #ffffff;
        gridline-color: #d4d0c8;
        font-family: "MS Sans Serif", Tahoma;
        font-size: 11px;
    }

    QTableWidget::item:selected {
        background-color: #000080;
        color: #ffffff;
    }

    QHeaderView::section {
        background-color: #d4d0c8;
        border-top: 2px solid #ffffff;
        border-left: 2px solid #ffffff;
        border-right: 2px solid #808080;
        border-bottom: 2px solid #808080;
        padding: 3px 6px;
        font-family: "MS Sans Serif", Tahoma;
        font-size: 11px;
    }

    /* Scrollbars */
    QScrollBar:vertical {
        background-color: #d4d0c8;
        width: 16px;
        border: 1px solid #808080;
    }

    QScrollBar::handle:vertical {
        background-color: #d4d0c8;
        border-top: 2px solid #ffffff;
        border-left: 2px solid #ffffff;
        border-right: 2px solid #808080;
        border-bottom: 2px solid #808080;
        min-height: 20px;
    }

    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        background-color: #d4d0c8;
        border-top: 2px solid #ffffff;
        border-left: 2px solid #ffffff;
        border-right: 2px solid #808080;
        border-bottom: 2px solid #808080;
        height: 16px;
    }

    QScrollBar:horizontal {
        background-color: #d4d0c8;
        height: 16px;
        border: 1px solid #808080;
    }

    QScrollBar::handle:horizontal {
        background-color: #d4d0c8;
        border-top: 2px solid #ffffff;
        border-left: 2px solid #ffffff;
        border-right: 2px solid #808080;
        border-bottom: 2px solid #808080;
        min-width: 20px;
    }

    /* Menu Bar */
    QMenuBar {
        background-color: #d4d0c8;
        font-family: "MS Sans Serif", Tahoma;
        font-size: 11px;
        border-bottom: 1px solid #808080;
    }

    QMenuBar::item:selected {
        background-color: #000080;
        color: #ffffff;
    }

    QMenu {
        background-color: #d4d0c8;
        border: 1px solid #808080;
        font-family: "MS Sans Serif", Tahoma;
        font-size: 11px;
    }

    QMenu::item:selected {
        background-color: #000080;
        color: #ffffff;
    }

    /* Toolbar separator frame */
    QFrame#toolbarSeparator {
        color: #808080;
        background-color: #808080;
    }

    /* Status bar label */
    QLabel#statusLabel {
        background-color: #d4d0c8;
        border-top: 2px solid #808080;
        border-left: 2px solid #808080;
        border-right: 2px solid #ffffff;
        border-bottom: 2px solid #ffffff;
        padding: 2px 6px;
        font-family: "MS Sans Serif", Tahoma;
        font-size: 11px;
    }
"""

