import sys
from PyQt5.QtWidgets import QApplication
from gui.Main import MainWindow


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
