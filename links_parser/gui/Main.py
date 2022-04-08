from PyQt5.QtWidgets import (QLabel, QLineEdit, QWidget, QGridLayout, QPushButton, QVBoxLayout,
                             QHBoxLayout, QProgressBar, QScrollArea, QListWidget, QTabWidget)

from .ParsePage import ParsePage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(0, 0, 750, 500)
        self.setWindowTitle('Links Parser')
        self.setup_widgets()
        self.show()

    def setup_widgets(self):
        self.main_layout = ParsePage().ui
        self.setLayout(self.main_layout)
