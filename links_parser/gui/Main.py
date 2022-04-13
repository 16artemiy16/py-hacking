from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QStatusBar, QWidget)

from .pages.parsing import ParsingScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(0, 0, 750, 500)
        self.setWindowTitle('Links Parser')
        self.setup_widgets()
        self.show()

    def setup_widgets(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)


        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.parsing_page = ParsingScreen()
        self.main_layout.addWidget(self.parsing_page)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
