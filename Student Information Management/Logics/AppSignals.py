from PySide6.QtCore import QObject, Signal


class AppSignals(QObject):
    """
    Global signal bus. Any widget can emit data_changed() after a successful
    add/update/delete, and any other widget can subscribe to reload itself —
    without the two widgets needing to know about each other directly.
    """
    data_changed = Signal()


# Single shared instance — import this same object everywhere
app_signals = AppSignals()