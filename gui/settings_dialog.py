# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from assets.res_rc import *
from PyQt6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QFrame, QPushButton

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(856, 489)
        SettingsDialog.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.frame = QFrame(SettingsDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(200, 0, 521, 491))
        self.frame.setStyleSheet(u"background-color: rgb(38, 38, 38)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.ok_btn = QPushButton(SettingsDialog)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(750, 380, 81, 81))
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
        self.add_server_btn = QPushButton(SettingsDialog)
        self.add_server_btn.setObjectName(u"add_server_btn")
        self.add_server_btn.setGeometry(QRect(20, 20, 161, 71))
        font1 = QFont()
        font1.setFamilies([u"PF DinDisplay Pro"])
        font1.setPointSize(22)
        self.add_server_btn.setFont(font1)
        self.add_server_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgbrgb(48, 48, 48);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(82, 165, 53);\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(36, 36, 36);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}")
        self.add_server_btn.setIconSize(QSize(35, 35))

        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.ok_btn.setToolTip(QCoreApplication.translate("SettingsDialog", u"<html><head/><body><p>Start</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ok_btn.setText(QCoreApplication.translate("SettingsDialog", u"OK", None))
#if QT_CONFIG(tooltip)
        self.add_server_btn.setToolTip(QCoreApplication.translate("SettingsDialog", u"<html><head/><body><p>Add Server</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.add_server_btn.setText(QCoreApplication.translate("SettingsDialog", u"UI", None))
    # retranslateUi

