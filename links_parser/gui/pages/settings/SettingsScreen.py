from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class SettingsScreen(QWidget):
    def __init__(self):
        super(SettingsScreen, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.main_layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setText('Settings')

        self.main_layout.addWidget(self.label)

        self.setLayout(self.main_layout)
