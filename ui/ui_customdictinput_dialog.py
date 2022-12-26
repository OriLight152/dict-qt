# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customdictinput_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_DialogCustomDictInput(object):
    def setupUi(self, DialogCustomDictInput):
        if not DialogCustomDictInput.objectName():
            DialogCustomDictInput.setObjectName(u"DialogCustomDictInput")
        DialogCustomDictInput.setWindowModality(Qt.WindowModal)
        DialogCustomDictInput.resize(246, 271)
        DialogCustomDictInput.setMinimumSize(QSize(246, 271))
        DialogCustomDictInput.setMaximumSize(QSize(246, 271))
        self.btn_y = QPushButton(DialogCustomDictInput)
        self.btn_y.setObjectName(u"btn_y")
        self.btn_y.setGeometry(QRect(20, 230, 71, 24))
        self.btn_n = QPushButton(DialogCustomDictInput)
        self.btn_n.setObjectName(u"btn_n")
        self.btn_n.setGeometry(QRect(150, 230, 71, 24))
        self.label = QLabel(DialogCustomDictInput)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 53, 16))
        self.label_2 = QLabel(DialogCustomDictInput)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 111, 16))
        self.lineEdit = QLineEdit(DialogCustomDictInput)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 30, 221, 21))
        self.textEdit = QTextEdit(DialogCustomDictInput)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 80, 221, 131))

        self.retranslateUi(DialogCustomDictInput)

        QMetaObject.connectSlotsByName(DialogCustomDictInput)
    # setupUi

    def retranslateUi(self, DialogCustomDictInput):
        DialogCustomDictInput.setWindowTitle(QCoreApplication.translate("DialogCustomDictInput", u"\u5bf9\u8bdd\u6846", None))
        self.btn_y.setText(QCoreApplication.translate("DialogCustomDictInput", u"\u786e\u5b9a", None))
        self.btn_n.setText(QCoreApplication.translate("DialogCustomDictInput", u"\u53d6\u6d88", None))
        self.label.setText(QCoreApplication.translate("DialogCustomDictInput", u"\u5355\u8bcd\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("DialogCustomDictInput", u"\u91ca\u4e49\uff08\u4e2d\u6587\uff09\uff1a", None))
    # retranslateUi

