from PyQt5.QtWidgets import (QWidget, QVBoxLayout)

from .pages.parsing import ParsingScreen


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
        self.main_layout = QVBoxLayout()

        self.parsing_page = ParsingScreen()
        self.main_layout.addWidget(self.parsing_page)

        self.setLayout(self.main_layout)
