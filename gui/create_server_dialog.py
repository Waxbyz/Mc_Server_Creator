# -*- coding: utf-8 -*-
import os
from pathlib import Path

from PySide6 import QtWidgets
################################################################################
## Form generated from reading UI file 'create_server_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QDragEnterEvent, QDropEvent)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
                               QLabel, QLineEdit, QProgressBar, QPushButton,
                               QSizePolicy, QWidget, QHBoxLayout, QFileDialog, QVBoxLayout)

from assets.res_rc import *

class FileDropButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/icon/icons/image_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setIcon(icon)
        self.setIconSize(QSize(50, 50))
        self.filename = ""
        self.filename1 = ""

        self.setStyleSheet("""
            QPushButton {
                background-color: rgb(44, 44, 44);
                border: 2px solid rgb(82, 165, 53);
                color: white;
                font-size: 14px;
                border-radius: 10px;
                padding: 12px;
            }
            QPushButton:hover {
                background-color: rgb(36, 36, 36);
            }
            QPushButton:pressed {
                background-color: rgb(25, 25, 25);
            }
        """)

        self.clicked.connect(self.choose_file)

    def choose_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '', 'Image Files (*.jpg *.jpeg *.png)')
        if file_path:
            self.save_image(file_path)
            icon2 = QIcon()
            icon2.addFile(u":/icon/icons/check_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal,
                          QIcon.State.Off)
            self.setIcon(icon2)
            self.setIconSize(QSize(50, 50))
            print(f"file_path is {file_path}")
        else:
            icon3 = QIcon()
            icon3.addFile(u":/icon/icons/close_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal,
                          QIcon.State.Off)
            self.setIcon(icon3)
            self.setIconSize(QSize(50, 50))

    def dragEnterEvent(self, event: QDragEnterEvent):
        for url in event.mimeData().urls():
            if os.path.splitext(url.toLocalFile())[1].lower() in ['.png', '.jpg', '.jpeg']:
                event.acceptProposedAction()
                return
        event.ignore()

    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            ext = os.path.splitext(file_path)[1].lower()
            if ext in ['.png', '.jpg', '.jpeg']:
                self.save_image(file_path)
                icon2 = QIcon()
                icon2.addFile(u":/icon/icons/check_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal,
                              QIcon.State.Off)
                self.setIcon(icon2)
                self.setIconSize(QSize(50, 50))
                print("image_accepted:", file_path)
                return
            icon3 = QIcon()
            icon3.addFile(u":/icon/icons/close_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal,
                          QIcon.State.Off)
            self.setIcon(icon3)
            self.setIconSize(QSize(50, 50))

    def save_image(self, file_path: str) -> None:
        target_dir = Path(os.getenv('APPDATA')) / ".mc_server_creator" / "images"
        target_dir.mkdir(parents=True, exist_ok=True)

        source_path = Path(file_path)
        target_path = target_dir / source_path.name

        target_path.write_bytes(source_path.read_bytes())
        print(f"Saved to {target_path}")

class Ui_CreateServerDialog(object):
    def setupUi(self, CreateServerDialog):
        if not CreateServerDialog.objectName():
            CreateServerDialog.setObjectName(u"CreateServerDialog")
        CreateServerDialog.resize(462, 520)
        CreateServerDialog.setStyleSheet(u"background-color: rgb(44, 44, 44);")

        font_id = QFontDatabase.addApplicationFont("../assets/fonts/Roboto-Medium.ttf")
        if font_id != -1:
            roboto_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        else:
            raise RuntimeError("Could not find Roboto font family.")

        self.ok_btn = QPushButton(CreateServerDialog)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(20, 420, 421, 71))
        font = QFont()
        font.setFamilies([u"PF DinDisplay Pro"])
        font.setPointSize(25)
        font.setBold(True)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(82, 165, 53);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 114, 36);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(30, 63, 19);\n"
"}")
        self.ok_btn.setIconSize(QSize(60, 60))
        self.frame = QFrame(CreateServerDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 201, 121))
        self.frame.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"border-radius: 9px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.name_lbl = QLabel(self.frame)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setGeometry(QRect(10, 10, 101, 31))
        font1 = QFont()
        font1.setFamilies([u"PF DinDisplay Pro"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.name_lbl.setFont(font1)
        self.name_lbl.setStyleSheet(u"background: None;\n"
"color: rgb(255, 255, 255)")
        self.name_btn = QLineEdit(self.frame)
        self.name_btn.setObjectName(u"name_btn")
        self.name_btn.setGeometry(QRect(10, 60, 181, 31))
        font2 = QFont()
        font2.setFamilies([roboto_family])
        font2.setPointSize(11)
        font2.setBold(False)
        self.name_btn.setFont(font2)
        self.name_btn.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"border-radius: 4px;\n"
"border: 2px solid rgb(82, 165, 53);\n"
"color: white")
        self.frame_2 = QFrame(CreateServerDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(240, 20, 201, 201))
        self.frame_2.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"border-radius: 9px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.core_lbl = QLabel(self.frame_2)
        self.core_lbl.setObjectName(u"core_lbl")
        self.core_lbl.setGeometry(QRect(10, 10, 101, 31))
        self.core_lbl.setFont(font1)
        self.core_lbl.setStyleSheet(u"background: None;\n"
"color: rgb(255, 255, 255)")
        self.loader_btn = QComboBox(self.frame_2)
        self.loader_btn.setObjectName(u"loader_btn")
        self.loader_btn.setGeometry(QRect(10, 80, 181, 31))
        font3 = QFont()
        font3.setFamilies([roboto_family])
        font3.setPointSize(11)
        self.loader_btn.setFont(font3)
        self.loader_btn.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(44, 44, 44);\n"
"    color: white;\n"
"    border: 2px solid rgb(82, 165, 53);\n"
"    border-radius: 4px;\n"
"    padding-right: 25px;\n"
"    selection-background-color: rgb(82, 165, 53);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    background-color: rgb(44, 44, 44);\n"
"    border-left: 2px solid rgb(82, 165, 53);\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/icons/arrow_drop_down_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg);\n"
"    width: 17px;\n"
"    height: 17px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: white;\n"
"    border: 1px solid rgb(82, 165, 53);\n"
"    outline: none;\n"
"    show-decoration-selected: 1;\n"
"    padding: 0;\n"
"    spacing: 0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"   "
                        " padding: 6px 10px;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgba(82, 165, 53);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(82, 165, 53);\n"
"    color: black;\n"
"    border-radius: 6px;\n"
                                      
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected:hover {\n"
"    background-color: rgb(82, 165, 53);\n"
"    color: black;\n"
"    border-left: 3px solid rgb(82, 165, 53);\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    background: rgb(44, 44, 44);\n"
"    width: 12px;\n"
"    margin: 2px 0;\n"
"    border: 1px solid rgb(82, 165, 53);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background: rgb(82, 165, 53);\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical:hover {\n"
""
                        "    background: rgb(82, 165, 53);\n"
"}\n"
"\n"
"QComboBox QScrollBar::add-line:vertical,\n"
"QComboBox QScrollBar::sub-line:vertical,\n"
"QComboBox QScrollBar::add-page:vertical,\n"
"QComboBox QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"}")
        self.loader_lbl = QLabel(self.frame_2)
        self.loader_lbl.setObjectName(u"loader_lbl")
        self.loader_lbl.setGeometry(QRect(10, 40, 171, 41))
        font4 = QFont()
        font4.setFamilies([u"PF DinDisplay Pro"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.loader_lbl.setFont(font4)
        self.loader_lbl.setStyleSheet(u"background: None;\n"
"color: rgb(255, 255, 255)")
        self.version_lbl = QLabel(self.frame_2)
        self.version_lbl.setObjectName(u"version_lbl")
        self.version_lbl.setGeometry(QRect(10, 110, 171, 41))
        self.version_lbl.setFont(font4)
        self.version_lbl.setStyleSheet(u"background: None;\n"
"color: rgb(255, 255, 255)")
        self.version_btn = QComboBox(self.frame_2)
        self.version_btn.setObjectName(u"version_btn")
        self.version_btn.setGeometry(QRect(10, 150, 181, 31))
        self.version_btn.setFont(font3)
        self.version_btn.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(44, 44, 44);\n"
"    color: white;\n"
"    border: 2px solid rgb(82, 165, 53);\n"
"    border-radius: 4px;\n"
"    padding-right: 25px;\n"
"    selection-background-color: rgb(82, 165, 53);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    background-color: rgb(44, 44, 44);\n"
"    border-left: 2px solid rgb(82, 165, 53);\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/icons/arrow_drop_down_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg);\n"
"    width: 17px;\n"
"    height: 17px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: white;\n"
"    border: 1px solid rgb(82, 165, 53);\n"
"    outline: none;\n"
"    show-decoration-selected: 1;\n"
"    padding: 0;\n"
"    spacing: 0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"   "
                        " padding: 6px 10px;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgba(82, 165, 53);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(82, 165, 53);\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected:hover {\n"
"    background-color: rgb(82, 165, 53);\n"
"    color: black;\n"
"    border-left: 3px solid rgb(82, 165, 53);\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    background: rgb(44, 44, 44);\n"
"    width: 12px;\n"
"    margin: 2px 0;\n"
"    border: 1px solid rgb(82, 165, 53);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background: rgb(82, 165, 53);\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical:hover {\n"
""
                        "    background: rgb(82, 165, 53);\n"
"}\n"
"\n"
"QComboBox QScrollBar::add-line:vertical,\n"
"QComboBox QScrollBar::sub-line:vertical,\n"
"QComboBox QScrollBar::add-page:vertical,\n"
"QComboBox QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"}")
        self.frame_3 = QFrame(CreateServerDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 240, 421, 161))
        self.frame_3.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 9px;")

        self.frame_4 = QFrame(CreateServerDialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 160, 201, 81))
        self.frame_4.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 0px;\n"
"\n"
"border-top-left-radius: 9px;\n"
"border-bottom-left-radius: 0px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.Image_lbl = QLabel(self.frame_4)
        self.Image_lbl.setObjectName(u"Image_lbl")
        self.Image_lbl.setGeometry(QRect(10, 10, 181, 51))
        font5 = QFont()
        font5.setFamilies([u"PF DinDisplay Pro"])
        font5.setPointSize(26)
        font5.setBold(True)
        self.Image_lbl.setFont(font5)
        self.Image_lbl.setStyleSheet(u"background: None;\n"
"color: rgb(255, 255, 255)")
        self.progressBar = QProgressBar(CreateServerDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 510, 461, 10))
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"background-color: rgb(38, 38, 38);\n"
"    border: none;\n"
"    max-height: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(82, 165, 53);\n"
"    border: none;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.retranslateUi(CreateServerDialog)

        QMetaObject.connectSlotsByName(CreateServerDialog)
    # setupUi

    def retranslateUi(self, CreateServerDialog):
        CreateServerDialog.setWindowTitle(QCoreApplication.translate("CreateServerDialog", u"Create server", None))
#if QT_CONFIG(tooltip)
        self.ok_btn.setToolTip(QCoreApplication.translate("CreateServerDialog", u"<html><head/><body><p>Start</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ok_btn.setText(QCoreApplication.translate("CreateServerDialog", u"OK", None))
        self.name_lbl.setText(QCoreApplication.translate("CreateServerDialog", u"Name:", None))
        self.core_lbl.setText(QCoreApplication.translate("CreateServerDialog", u"Core:", None))
        self.loader_lbl.setText(QCoreApplication.translate("CreateServerDialog", u"Loader:", None))
        self.version_lbl.setText(QCoreApplication.translate("CreateServerDialog", u"Version:", None))
        self.Image_lbl.setText(QCoreApplication.translate("CreateServerDialog", u"Image:", None))
        self.progressBar.setFormat("")
    # retranslateUi

