from PyQt5.QtWidgets import (QWidget, QVBoxLayout)
from .ParsingTabContent import ParsingTabContent
from links_parser.gui.pages.parsing.ParsingTabs import ParsingTabs


class ParsingScreen(QWidget):
    def __init__(self, new_tab_emitter):
        super().__init__()
        self.init_ui()

        new_tab_emitter.connect(self.create_new_parsing_tab)

    def init_ui(self):
        self.setup_widgets()
        self.create_new_parsing_tab()

    def setup_widgets(self):
        self.tab_bar = ParsingTabs()
        self.tab_bar.create_page_clicked.connect(self.create_new_parsing_tab)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addWidget(self.tab_bar.ui)
        self.setLayout(self.main_layout)

    def create_new_parsing_tab(self):
        widget = QWidget()
        widget.setLayout(ParsingTabContent().ui)
        self.tab_bar.add_tab(widget, f'New', active=True)
