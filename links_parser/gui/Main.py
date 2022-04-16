from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QStatusBar, QWidget, QTabWidget, QAction)
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import QIcon

from . import resources
from .pages.parsing import ParsingScreen
from .pages.settings import SettingsScreen


class MainWindow(QMainWindow):
    new_parsing_tab_emitter = pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(0, 0, 750, 500)
        self.setWindowTitle('Links Parser')
        self.setup_widgets()
        self.setup_menu()
        self.setup_left_tabs()
        self.show()

    def setup_widgets(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)

    def setup_menu(self):
        menubar = self.menuBar()
        m_parsing = menubar.addMenu(' &Parsing')

        a_parsing_new = QAction(' &New', self)
        a_parsing_new.setShortcut('Ctrl+N')
        a_parsing_new.setStatusTip('Open new parsing tab')
        a_parsing_new.triggered.connect(lambda: self.new_parsing_tab_emitter.emit())

        m_parsing.addAction(a_parsing_new)

    def setup_left_tabs(self):
        self.parsing_page = ParsingScreen(self.new_parsing_tab_emitter)
        self.settings_page = SettingsScreen()

        self.left_tabs = QTabWidget()
        self.left_tabs.setObjectName('left-tabs')
        self.left_tabs.setTabPosition(QTabWidget.West)
        self.left_tabs.addTab(self.parsing_page, QIcon(':network.svg'), '')
        self.left_tabs.addTab(self.settings_page, QIcon(':settings.svg'), '')

        self.left_tabs.setTabToolTip(0, 'Parsing')
        self.left_tabs.setTabToolTip(1, 'Settings')
        self.left_tabs.tabBar().setCursor(Qt.PointingHandCursor)

        self.left_tabs.setIconSize(QSize(35, 35))
        self.left_tabs.setStyleSheet('''
        QTabWidget#left-tabs::tab-bar {
            alignment: left;
            background-color: red;
        }
        QTabWidget#left-tabs > QTabBar::tab {
            background-color: #F8F8FF;
            height: 70px;
            width: 70px;
            border: none;
            margin: 0px;
            padding-top: -15px;
            padding-bottom: 15px
        }
        QTabWidget#left-tabs > QTabBar::tab:selected {
            background-color: #0276FD;
        }
        QTabWidget#left-tabs > QTabBar::tab:hover {
            background-color: #6495ED;
        }
        ''')

        self.main_layout.addWidget(self.left_tabs)
