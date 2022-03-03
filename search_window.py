# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(400, 600)
        SearchWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchEdit.setGeometry(QtCore.QRect(30, 110, 300, 40))
        self.SearchEdit.setAutoFillBackground(False)
        self.SearchEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SearchEdit.setObjectName("SearchEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 180, 300, 400))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(55)
        self.change_page_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_page_button.setGeometry(QtCore.QRect(270, 36, 48, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_page_button.sizePolicy().hasHeightForWidth())
        self.change_page_button.setSizePolicy(sizePolicy)
        self.change_page_button.setMinimumSize(QtCore.QSize(48, 48))
        self.change_page_button.setMaximumSize(QtCore.QSize(48, 48))
        self.change_page_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/images/ico/add_to_list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_page_button.setIcon(icon)
        self.change_page_button.setIconSize(QtCore.QSize(48, 48))
        self.change_page_button.setFlat(True)
        self.change_page_button.setObjectName("change_page_button")
        self.disc_3 = QtWidgets.QLabel(self.centralwidget)
        self.disc_3.setEnabled(True)
        self.disc_3.setGeometry(QtCore.QRect(30, 20, 64, 64))
        self.disc_3.setMinimumSize(QtCore.QSize(64, 64))
        self.disc_3.setMaximumSize(QtCore.QSize(64, 64))
        self.disc_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.disc_3.setText("")
        self.disc_3.setPixmap(QtGui.QPixmap("images/ico/disc.png"))
        self.disc_3.setObjectName("disc_3")
        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "SearchWindow"))
        self.SearchEdit.setPlaceholderText(_translate("SearchWindow", "请搜索"))
        self.change_page_button.setToolTip(_translate("SearchWindow", ""))
