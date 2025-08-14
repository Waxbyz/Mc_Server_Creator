import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

from create_server_dialog import Ui_CreateServerDialog
from mc_server_creator import Ui_ServerCreator
from server_creator.versions_getter import *

class CreateServerDialog(QtWidgets.QDialog, Ui_CreateServerDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('../assets/logo/msc_logo.png'))
        self.setFixedSize(self.size())
        self.loader_btn.setMaxVisibleItems(7)
        self.version_btn.setMaxVisibleItems(7)

        self.load_versions()

    def load_versions(self):
        getter = VanillaVersionsGetter([])
        try:
            versions = getter.get_version()

            def version_key(v):
                return [int(part) if part.isdigit() else 0 for part in v.split(".")]

            versions.sort(key=version_key, reverse=True)

            self.version_btn.clear()
            self.version_btn.addItems(versions)
            self.version_btn.setInsertPolicy(QComboBox.NoInsert)
        except Exception as e:
            print(f"Error when loading versions: {e}")
            self.version_btn.addItem("Error Loading")

class ServerCreator(QMainWindow, Ui_ServerCreator):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ServerCreator()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('../assets/logo/msc_logo.png'))

        self.ui.add_server_btn.clicked.connect(self.open_create_server_window)

    def open_create_server_window(self):
        self.create_server_dialog = CreateServerDialog()
        self.create_server_dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerCreator()
    window.show()

    sys.exit(app.exec())