# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(954, 718)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/ms_icon.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.action_dark_mode = QAction(MainWindow)
        self.action_dark_mode.setObjectName(u"action_dark_mode")
        self.action_dark_mode.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_mongo_url = QLineEdit(self.groupBox_3)
        self.line_mongo_url.setObjectName(u"line_mongo_url")

        self.horizontalLayout_4.addWidget(self.line_mongo_url)

        self.line_mongo_username = QLineEdit(self.groupBox_3)
        self.line_mongo_username.setObjectName(u"line_mongo_username")

        self.horizontalLayout_4.addWidget(self.line_mongo_username)

        self.line_mongo_password = QLineEdit(self.groupBox_3)
        self.line_mongo_password.setObjectName(u"line_mongo_password")
        self.line_mongo_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_4.addWidget(self.line_mongo_password)

        self.radio_on_mongo_cloud = QRadioButton(self.groupBox_3)
        self.radio_on_mongo_cloud.setObjectName(u"radio_on_mongo_cloud")

        self.horizontalLayout_4.addWidget(self.radio_on_mongo_cloud)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.line_mongo_database = QLineEdit(self.groupBox_3)
        self.line_mongo_database.setObjectName(u"line_mongo_database")

        self.horizontalLayout_5.addWidget(self.line_mongo_database)

        self.line_mongo_collection = QLineEdit(self.groupBox_3)
        self.line_mongo_collection.setObjectName(u"line_mongo_collection")

        self.horizontalLayout_5.addWidget(self.line_mongo_collection)

        self.button_db_connect = QPushButton(self.groupBox_3)
        self.button_db_connect.setObjectName(u"button_db_connect")

        self.horizontalLayout_5.addWidget(self.button_db_connect)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_username = QLineEdit(self.groupBox)
        self.line_username.setObjectName(u"line_username")

        self.horizontalLayout.addWidget(self.line_username)

        self.line_password = QLineEdit(self.groupBox)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout.addWidget(self.line_password)

        self.button_user_connect = QPushButton(self.groupBox)
        self.button_user_connect.setObjectName(u"button_user_connect")

        self.horizontalLayout.addWidget(self.button_user_connect)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_add_user = QLineEdit(self.groupBox_2)
        self.line_add_user.setObjectName(u"line_add_user")

        self.horizontalLayout_2.addWidget(self.line_add_user)

        self.line_add_password = QLineEdit(self.groupBox_2)
        self.line_add_password.setObjectName(u"line_add_password")
        self.line_add_password.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout_2.addWidget(self.line_add_password)

        self.button_add = QPushButton(self.groupBox_2)
        self.button_add.setObjectName(u"button_add")

        self.horizontalLayout_2.addWidget(self.button_add)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.line_user_search = QLineEdit(self.groupBox_4)
        self.line_user_search.setObjectName(u"line_user_search")

        self.horizontalLayout_6.addWidget(self.line_user_search)

        self.button_search = QPushButton(self.groupBox_4)
        self.button_search.setObjectName(u"button_search")

        self.horizontalLayout_6.addWidget(self.button_search)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.button_delete = QPushButton(self.groupBox_4)
        self.button_delete.setObjectName(u"button_delete")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_delete.sizePolicy().hasHeightForWidth())
        self.button_delete.setSizePolicy(sizePolicy1)
        self.button_delete.setMinimumSize(QSize(100, 0))
        self.button_delete.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.button_delete)

        self.table = QTableWidget(self.groupBox_4)
        self.table.setObjectName(u"table")

        self.verticalLayout_3.addWidget(self.table)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.label_connection = QLabel(self.centralwidget)
        self.label_connection.setObjectName(u"label_connection")

        self.verticalLayout_4.addWidget(self.label_connection)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 954, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.line_mongo_url, self.line_mongo_database)
        QWidget.setTabOrder(self.line_mongo_database, self.line_mongo_collection)
        QWidget.setTabOrder(self.line_mongo_collection, self.line_mongo_username)
        QWidget.setTabOrder(self.line_mongo_username, self.line_mongo_password)
        QWidget.setTabOrder(self.line_mongo_password, self.button_db_connect)
        QWidget.setTabOrder(self.button_db_connect, self.line_username)
        QWidget.setTabOrder(self.line_username, self.line_password)
        QWidget.setTabOrder(self.line_password, self.button_user_connect)
        QWidget.setTabOrder(self.button_user_connect, self.line_add_user)
        QWidget.setTabOrder(self.line_add_user, self.line_add_password)
        QWidget.setTabOrder(self.line_add_password, self.button_add)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.action_about)
        self.menuHelp.addAction(self.action_about_qt)
        self.menuSettings.addAction(self.action_dark_mode)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"User Login Creation Tool", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.action_dark_mode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Connect to Database", None))
#if QT_CONFIG(statustip)
        self.line_mongo_url.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter the URL for your MongoDB cloud instance", None))
#endif // QT_CONFIG(statustip)
        self.line_mongo_url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MongoDB URL", None))
#if QT_CONFIG(statustip)
        self.line_mongo_username.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter the MongoDB user", None))
#endif // QT_CONFIG(statustip)
        self.line_mongo_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Database Username", None))
#if QT_CONFIG(statustip)
        self.line_mongo_password.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter the password to access the database", None))
#endif // QT_CONFIG(statustip)
        self.line_mongo_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Database Password", None))
#if QT_CONFIG(statustip)
        self.radio_on_mongo_cloud.setStatusTip(QCoreApplication.translate("MainWindow", u"Will connect to MongoDB Cloud if checked", None))
#endif // QT_CONFIG(statustip)
        self.radio_on_mongo_cloud.setText(QCoreApplication.translate("MainWindow", u"MongoDB Cloud", None))
#if QT_CONFIG(statustip)
        self.line_mongo_database.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter the database name, a new database will be created automatically (if needed)", None))
#endif // QT_CONFIG(statustip)
        self.line_mongo_database.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Database", None))
#if QT_CONFIG(statustip)
        self.line_mongo_collection.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter the collection name, a new collection will be created automatically (if needed)", None))
#endif // QT_CONFIG(statustip)
        self.line_mongo_collection.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Collection", None))
        self.button_db_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"User Login", None))
#if QT_CONFIG(statustip)
        self.line_username.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter a registered user to test hello world", None))
#endif // QT_CONFIG(statustip)
        self.line_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User email", None))
#if QT_CONFIG(statustip)
        self.line_password.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter a registered user's password to test hello world", None))
#endif // QT_CONFIG(statustip)
        self.line_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.button_user_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Register a new user", None))
#if QT_CONFIG(statustip)
        self.line_add_user.setStatusTip(QCoreApplication.translate("MainWindow", u"Register a new user for hello world", None))
#endif // QT_CONFIG(statustip)
        self.line_add_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User email", None))
#if QT_CONFIG(statustip)
        self.line_add_password.setStatusTip(QCoreApplication.translate("MainWindow", u"Register a password for the new user for hello world", None))
#endif // QT_CONFIG(statustip)
        self.line_add_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Registered Users", None))
#if QT_CONFIG(statustip)
        self.line_user_search.setStatusTip(QCoreApplication.translate("MainWindow", u"Search for specific user", None))
#endif // QT_CONFIG(statustip)
        self.line_user_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for user", None))
#if QT_CONFIG(statustip)
        self.button_search.setStatusTip(QCoreApplication.translate("MainWindow", u"Search for user (returns all users in the database if blank)", None))
#endif // QT_CONFIG(statustip)
        self.button_search.setText(QCoreApplication.translate("MainWindow", u"Search Database", None))
#if QT_CONFIG(statustip)
        self.button_delete.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete highlisted user from the database", None))
#endif // QT_CONFIG(statustip)
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"Delete User", None))
#if QT_CONFIG(statustip)
        self.table.setStatusTip(QCoreApplication.translate("MainWindow", u"Displays all the registered users in the database", None))
#endif // QT_CONFIG(statustip)
        self.label_connection.setText(QCoreApplication.translate("MainWindow", u"MongoDB Connection Label", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

