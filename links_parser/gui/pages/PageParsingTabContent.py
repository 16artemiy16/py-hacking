from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget
from PyQt5.QtCore import Qt

import sys, os
sys.path.insert(0, os.path.abspath('..'))

from links_parser.links_extractor import LinksExtractor


class PageParsingTabContent(QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()

    @property
    def ui(self):
        return self.main_layout

    def _init_ui(self):
        self.main_layout = QVBoxLayout()
        self._set_input_layout()
        self._set_results_layout()
        self.setLayout(self.main_layout)

    def _set_input_layout(self):
        """ Input layout """
        self.input_layout = QHBoxLayout()
        self.input_layout.setAlignment(Qt.AlignTop)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('Enter URL to parse')

        self.parse_btn = QPushButton('Parse')
        self.parse_btn.clicked.connect(lambda: self._parse_links(self.url_input.text()))

        self.input_layout.addWidget(self.url_input)
        self.input_layout.addWidget(self.parse_btn)

        self.main_layout.addLayout(self.input_layout)

    def _set_results_layout(self):
        self.results_layout = QVBoxLayout()
        self.results_layout.setAlignment(Qt.AlignTop)

        self.results_list = QListWidget()
        self.results_layout.addWidget(self.results_list)

        self.main_layout.addLayout(self.results_layout)

    def _parse_links(self, url):
        result = LinksExtractor(url).fetch()
        for url in result.external:
            self.results_list.addItem(url)
