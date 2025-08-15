# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mc_server_creator.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QTableView, QWidget)
from assets.res_rc import *

class Ui_ServerCreator(object):
    def setupUi(self, ServerCreator):
        if not ServerCreator.objectName():
            ServerCreator.setObjectName(u"ServerCreator")
        ServerCreator.resize(1047, 556)
        ServerCreator.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.centralwidget = QWidget(ServerCreator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, -10, 231, 101))
        self.groupBox.setStyleSheet(u"border: None;\n"
"background-color: rgb(36, 36, 36)")
        self.delete_server_btn = QPushButton(self.groupBox)
        self.delete_server_btn.setObjectName(u"delete_server_btn")
        self.delete_server_btn.setGeometry(QRect(160, 30, 51, 51))
        self.delete_server_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(48, 48, 48);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(82, 165, 53);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(36, 36, 36);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/delete_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_server_btn.setIcon(icon)
        self.delete_server_btn.setIconSize(QSize(35, 35))
        self.change_server_btn = QPushButton(self.groupBox)
        self.change_server_btn.setObjectName(u"change_server_btn")
        self.change_server_btn.setGeometry(QRect(90, 30, 51, 51))
        self.change_server_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(48, 48, 48);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(82, 165, 53);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(36, 36, 36);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/edit_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.change_server_btn.setIcon(icon1)
        self.change_server_btn.setIconSize(QSize(35, 35))
        self.add_server_btn = QPushButton(self.groupBox)
        self.add_server_btn.setObjectName(u"add_server_btn")
        self.add_server_btn.setGeometry(QRect(20, 30, 51, 51))
        self.add_server_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(48, 48, 48);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(82, 165, 53);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(36, 36, 36);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/add_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_server_btn.setIcon(icon2)
        self.add_server_btn.setIconSize(QSize(35, 35))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 90, 231, 471))
        self.scrollArea.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"border: None")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 231, 471))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(940, 450, 81, 81))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(82, 165, 53);\n"
"	border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(56, 114, 36);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(30, 63, 19);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/play_arrow_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_btn.setIcon(icon3)
        self.start_btn.setIconSize(QSize(60, 60))
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(230, 0, 671, 631))
        self.tableView.setStyleSheet(u"border: None;\n"
"background-color: rgb(38, 38, 38)")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(320, -30, 481, 161))
        self.logo.setStyleSheet(u"background-color: None")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(900, -10, 161, 101))
        self.groupBox_2.setStyleSheet(u"border: None;\n"
"background-color: rgb(36, 36, 36)")
        self.settings_btn = QPushButton(self.groupBox_2)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setGeometry(QRect(40, 30, 71, 51))
        self.settings_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(48, 48, 48);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(82, 165, 53);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(36, 36, 36);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/settings_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_btn.setIcon(icon4)
        self.settings_btn.setIconSize(QSize(40, 40))
        ServerCreator.setCentralWidget(self.centralwidget)

        self.retranslateUi(ServerCreator)

        QMetaObject.connectSlotsByName(ServerCreator)
    # setupUi

    def retranslateUi(self, ServerCreator):
        ServerCreator.setWindowTitle(QCoreApplication.translate("ServerCreator", u"MC Server Creator", None))
        self.groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.delete_server_btn.setToolTip(QCoreApplication.translate("ServerCreator", u"<html><head/><body><p>Delete Server</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delete_server_btn.setText("")
#if QT_CONFIG(tooltip)
        self.change_server_btn.setToolTip(QCoreApplication.translate("ServerCreator", u"<html><head/><body><p>Change Server</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.change_server_btn.setText("")
#if QT_CONFIG(tooltip)
        self.add_server_btn.setToolTip(QCoreApplication.translate("ServerCreator", u"<html><head/><body><p>Add Server</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.add_server_btn.setText("")
#if QT_CONFIG(tooltip)
        self.start_btn.setToolTip(QCoreApplication.translate("ServerCreator", u"<html><head/><body><p>Start</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.start_btn.setText("")
#if QT_CONFIG(tooltip)
        self.logo.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.logo.setText(QCoreApplication.translate("ServerCreator", u"<html><head/><body><p><img src=\":/logo/logo/minecraft_title2.png\"/></p></body></html>", None))
        self.groupBox_2.setTitle("")
#if QT_CONFIG(tooltip)
        self.settings_btn.setToolTip(QCoreApplication.translate("ServerCreator", u"<html><head/><body><p>Settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settings_btn.setText("")
    # retranslateUi

