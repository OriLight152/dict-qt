# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customdictmanager_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_CustomDictManager(object):
    def setupUi(self, Dialog_CustomDictManager):
        if not Dialog_CustomDictManager.objectName():
            Dialog_CustomDictManager.setObjectName(u"Dialog_CustomDictManager")
        Dialog_CustomDictManager.setWindowModality(Qt.WindowModal)
        Dialog_CustomDictManager.resize(331, 300)
        Dialog_CustomDictManager.setMinimumSize(QSize(331, 300))
        Dialog_CustomDictManager.setMaximumSize(QSize(331, 300))
        self.btn_save = QPushButton(Dialog_CustomDictManager)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(10, 260, 71, 31))
        self.btn_add = QPushButton(Dialog_CustomDictManager)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(90, 260, 71, 31))
        self.btn_add.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_del = QPushButton(Dialog_CustomDictManager)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setGeometry(QRect(170, 260, 71, 31))
        self.btn_del.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_edit = QPushButton(Dialog_CustomDictManager)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setGeometry(QRect(250, 260, 71, 31))
        self.btn_edit.setCursor(QCursor(Qt.ArrowCursor))
        self.listWidget = QListWidget(Dialog_CustomDictManager)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 10, 311, 241))

        self.retranslateUi(Dialog_CustomDictManager)

        QMetaObject.connectSlotsByName(Dialog_CustomDictManager)
    # setupUi

    def retranslateUi(self, Dialog_CustomDictManager):
        Dialog_CustomDictManager.setWindowTitle(QCoreApplication.translate("Dialog_CustomDictManager", u"\u81ea\u5b9a\u4e49\u8bcd\u5178\u7ba1\u7406", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog_CustomDictManager", u"\u4fdd\u5b58", None))
        self.btn_add.setText(QCoreApplication.translate("Dialog_CustomDictManager", u"\u65b0\u589e", None))
        self.btn_del.setText(QCoreApplication.translate("Dialog_CustomDictManager", u"\u5220\u9664", None))
        self.btn_edit.setText(QCoreApplication.translate("Dialog_CustomDictManager", u"\u7f16\u8f91", None))
    # retranslateUi

