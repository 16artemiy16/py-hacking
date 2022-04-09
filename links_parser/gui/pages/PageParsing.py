from PyQt5.QtWidgets import (QWidget, QVBoxLayout)
from .PageParsingTabContent import PageParsingTabContent
from links_parser.gui.pages.PageParsingTabs import PageParsingTabs


class PageParsing(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(0, 0, 750, 500)
        self.setWindowTitle('Links Parser')
        self.setup_widgets()

        self.create_new_parsing_tab()


    def setup_widgets(self):
        self.tab_bar = PageParsingTabs()
        self.tab_bar.create_page_clicked.connect(self.create_new_parsing_tab)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.tab_bar.ui)
        self.setLayout(self.main_layout)

    def create_new_parsing_tab(self):
        widget = QWidget()
        widget.setLayout(PageParsingTabContent().ui)
        self.tab_bar.add_tab(widget, f'New')
