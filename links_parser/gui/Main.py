from PyQt5.QtWidgets import (QLabel, QLineEdit, QWidget, QGridLayout, QPushButton, QVBoxLayout,
                             QHBoxLayout, QProgressBar, QScrollArea, QListWidget, QTabWidget)

from .ParsePage import ParsePage
from .MainTabBar import MainTabBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(0, 0, 750, 500)
        self.setWindowTitle('Links Parser')
        self.setup_widgets()

        self.create_new_parsing_tab()

        self.show()

    def setup_widgets(self):
        self.tab_bar = MainTabBar()
        self.tab_bar.create_page_clicked.connect(self.create_new_parsing_tab)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.tab_bar.ui)
        self.setLayout(self.main_layout)

    def create_new_parsing_tab(self):
        widget = QWidget()
        widget.setLayout(ParsePage().ui)
        self.tab_bar.add_tab(widget, f'New')
