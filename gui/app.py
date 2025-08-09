import sys
import time

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

from mc_server_creator import Ui_ServerCreator

class ServerCreator(QMainWindow, Ui_ServerCreator):
    def __init__(self):
        super().__init__()

        self.ui = Ui_ServerCreator()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('../assets/logo/msc_logo.png'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerCreator()
    window.show()

    sys.exit(app.exec())