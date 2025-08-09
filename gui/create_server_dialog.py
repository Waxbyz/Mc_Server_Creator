# -*- coding: utf-8 -*-

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
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QWidget)
from assets.res_rc import *

class Ui_CreateServerDialog(object):
    def setupUi(self, CreateServerDialog):
        if not CreateServerDialog.objectName():
            CreateServerDialog.setObjectName(u"CreateServerDialog")
        CreateServerDialog.resize(462, 520)
        CreateServerDialog.setStyleSheet(u"background-color: rgb(44, 44, 44);")
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
        font2.setFamilies([u"Roboto Medium"])
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
        font3.setFamilies([u"Roboto Medium"])
        font3.setPointSize(11)
        self.loader_btn.setFont(font3)
        self.loader_btn.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(44, 44, 44);\n"
"	color: white;\n"
"    border: 2px solid rgb(82, 165, 53);\n"
"    border-radius: 4px;\n"
"    padding-right: 25px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    background-color: rgb(44, 44, 44);\n"
"    border-left: 2px solid rgb(82, 165, 53);\n"
"\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/icons/arrow_drop_down_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg); \n"
"    width: 17px;\n"
"    height: 17px;\n"
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
"	color: white;\n"
"    border: 2px solid rgb(82, 165, 53);\n"
"    border-radius: 4px;\n"
"    padding-right: 25px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    background-color: rgb(44, 44, 44);\n"
"    border-left: 2px solid rgb(82, 165, 53);\n"
"\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icon/icons/arrow_drop_down_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg); \n"
"    width: 17px;\n"
"    height: 17px;\n"
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
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.choose_file_lbl = QLabel(self.frame_3)
        self.choose_file_lbl.setObjectName(u"choose_file_lbl")
        self.choose_file_lbl.setGeometry(QRect(10, 0, 171, 41))
        self.choose_file_lbl.setFont(font4)
        self.choose_file_lbl.setStyleSheet(u"background: None;\n"
"color: rgb(255, 255, 255)")
        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(210, 10, 2, 141))
        self.line.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"min-width: 2px;\n"
"max-width: 2px;\n"
"border-radius: 1px;")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.drag_and_drop_lbl = QLabel(self.frame_3)
        self.drag_and_drop_lbl.setObjectName(u"drag_and_drop_lbl")
        self.drag_and_drop_lbl.setGeometry(QRect(230, 0, 171, 41))
        self.drag_and_drop_lbl.setFont(font4)
        self.drag_and_drop_lbl.setStyleSheet(u"background: None;\n"
"color: rgb(255, 255, 255)")
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
        self.choose_file_lbl.setText(QCoreApplication.translate("CreateServerDialog", u"Choose file:", None))
        self.drag_and_drop_lbl.setText(QCoreApplication.translate("CreateServerDialog", u"Drag and Drop:", None))
        self.Image_lbl.setText(QCoreApplication.translate("CreateServerDialog", u"Image:", None))
        self.progressBar.setFormat("")
    # retranslateUi

