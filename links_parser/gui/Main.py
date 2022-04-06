from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

import sys, os
sys.path.insert(0, os.path.abspath('..'))

from links_parser.links_extractor import LinksExtractor


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(500, 500, 300, 300)
        self.setWindowTitle('Links Parser')
        self.setup_widgets()
        self.show()

    def setup_widgets(self):
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.input_layout)

        self.setLayout(main_layout)

    @property
    def input_layout(self):
        """ Input layout """
        input_layout = QHBoxLayout()
        input_layout.setAlignment(Qt.AlignTop)

        url_input = QLineEdit()
        url_input.setPlaceholderText('Enter URL to parse')

        parse_btn = QPushButton('Parse')
        parse_btn.clicked.connect(lambda: self.parse_links(url_input.text()))

        input_layout.addWidget(url_input)
        input_layout.addWidget(parse_btn)

        return input_layout

    def parse_links(self, url):
        pass
