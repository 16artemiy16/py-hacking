from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget
from PyQt5.QtCore import Qt
import threading

import sys, os
sys.path.insert(0, os.path.abspath('..'))

from links_parser.links_extractor import LinksExtractor


class ParsingTabContent(QWidget):
    def __init__(self):
        super(ParsingTabContent, self).__init__()
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
        self.input_layout = QHBoxLayout()
        self.input_layout.setAlignment(Qt.AlignTop)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('Enter URL to parse')
        self.url_input.textChanged.connect(self._watch_url_change)

        self.parse_btn = QPushButton('Parse')
        self.parse_btn.clicked.connect(lambda: self._parse_links_threading(self.url_input.text()))
        self.parse_btn.setEnabled(False)

        self.input_layout.addWidget(self.url_input)
        self.input_layout.addWidget(self.parse_btn)

        self.main_layout.addLayout(self.input_layout)

    def _set_results_layout(self):
        self.results_layout = QVBoxLayout()
        self.results_layout.setAlignment(Qt.AlignTop)

        self.results_list = QListWidget()
        self.results_layout.addWidget(self.results_list)

        self.main_layout.addLayout(self.results_layout)

    def _watch_url_change(self, value):
        is_empty = len(value.strip()) == 0
        self.parse_btn.setEnabled(not is_empty)

    def _parse_links_sync(self, url):
        self.results_list.clear()
        result = LinksExtractor(url).fetch()
        for url in result.external:
            self.results_list.addItem(url)

    def _parse_links_threading(self, url):
        t = threading.Thread(target=self._parse_links_sync, args=(url,))
        t.start()
