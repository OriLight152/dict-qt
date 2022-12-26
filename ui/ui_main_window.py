# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 312)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 312))
        MainWindow.setMaximumSize(QSize(700, 312))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(10, 10, 251, 21))
        self.edit_search = QLineEdit(self.centralwidget)
        self.edit_search.setObjectName(u"edit_search")
        self.edit_search.setGeometry(QRect(10, 40, 351, 31))
        self.label_translation = QLabel(self.centralwidget)
        self.label_translation.setObjectName(u"label_translation")
        self.label_translation.setGeometry(QRect(400, 80, 290, 220))
        self.label_translation.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_translation.setWordWrap(True)
        self.list_search = QListWidget(self.centralwidget)
        self.list_search.setObjectName(u"list_search")
        self.list_search.setGeometry(QRect(10, 70, 381, 231))
        self.label_word = QLabel(self.centralwidget)
        self.label_word.setObjectName(u"label_word")
        self.label_word.setGeometry(QRect(400, 40, 291, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_word.setFont(font)
        self.option_enablefuzzysearch = QCheckBox(self.centralwidget)
        self.option_enablefuzzysearch.setObjectName(u"option_enablefuzzysearch")
        self.option_enablefuzzysearch.setGeometry(QRect(400, 10, 291, 21))
        self.btn_search = QPushButton(self.centralwidget)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(360, 40, 31, 31))
        self.text_definition = QTextBrowser(self.centralwidget)
        self.text_definition.setObjectName(u"text_definition")
        self.text_definition.setGeometry(QRect(400, 70, 291, 231))
        self.btn_opencustomdictmanager = QPushButton(self.centralwidget)
        self.btn_opencustomdictmanager.setObjectName(u"btn_opencustomdictmanager")
        self.btn_opencustomdictmanager.setGeometry(QRect(260, 10, 131, 21))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u82f1\u6c49\u5c0f\u8bcd\u5178", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_translation.setText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1", None))
        self.label_word.setText(QCoreApplication.translate("MainWindow", u"\u5355\u8bcd", None))
#if QT_CONFIG(tooltip)
        self.option_enablefuzzysearch.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.option_enablefuzzysearch.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u7cca\u641c\u7d22\uff08\u53ef\u80fd\u4f1a\u589e\u52a0\u641c\u7d22\u7528\u65f6\u6216\u5bfc\u81f4\u7a0b\u5e8f\u5d29\u6e83\uff09", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"\u641c", None))
        self.btn_opencustomdictmanager.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u81ea\u5b9a\u4e49\u8bcd\u5178\u6570\u636e", None))
    # retranslateUi

