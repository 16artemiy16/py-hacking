from PyQt5.QtWidgets import QWidget, QTabWidget, QToolButton
from PyQt5.QtCore import pyqtSlot, pyqtSignal


class ParsingTabs(QWidget):
    create_page_clicked = pyqtSignal()
    _styles = '''
        QTabWidget::tab-bar {
            alignment: left;
        }
        '''

    def __init__(self):
        super().__init__()
        self._init()

    @property
    def ui(self):
        return self._tab_bar

    def _init(self):
        self._tab_bar = QTabWidget()
        self._tab_bar.setTabsClosable(True)
        self._tab_bar.setStyleSheet(self._styles)

        self._plus_btn = QToolButton(self)
        self._plus_btn.setText('+')

        self._tab_bar.setCornerWidget(self._plus_btn)
        self._plus_btn.clicked.connect(lambda: self.create_page_clicked.emit())

    def add_tab(self, *args):
        self._tab_bar.addTab(*args)
