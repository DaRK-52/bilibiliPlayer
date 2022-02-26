# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 800)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 619, 571, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_mode_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.play_mode_button.setStyleSheet("")
        self.play_mode_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/random.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_mode_button.setIcon(icon)
        self.play_mode_button.setIconSize(QtCore.QSize(30, 30))
        self.play_mode_button.setFlat(True)
        self.play_mode_button.setObjectName("play_mode_button")
        self.horizontalLayout.addWidget(self.play_mode_button)
        self.previous_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.previous_button.setStyleSheet("")
        self.previous_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/24gf-previousFrame.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_button.setIcon(icon1)
        self.previous_button.setIconSize(QtCore.QSize(30, 30))
        self.previous_button.setFlat(True)
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout.addWidget(self.previous_button)
        self.play_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.play_button.setStyleSheet("")
        self.play_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/24gf-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon2)
        self.play_button.setIconSize(QtCore.QSize(30, 30))
        self.play_button.setFlat(True)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout.addWidget(self.play_button)
        self.next_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.next_button.setStyleSheet("")
        self.next_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./images/24gf-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon3)
        self.next_button.setIconSize(QtCore.QSize(30, 30))
        self.next_button.setFlat(True)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.play_table_song_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.play_table_song_button.setStyleSheet("")
        self.play_table_song_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./images/24gf-playlistMusic4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_table_song_button.setIcon(icon4)
        self.play_table_song_button.setIconSize(QtCore.QSize(30, 30))
        self.play_table_song_button.setFlat(True)
        self.play_table_song_button.setObjectName("play_table_song_button")
        self.horizontalLayout.addWidget(self.play_table_song_button)
        self.song_title = QtWidgets.QLabel(self.centralwidget)
        self.song_title.setGeometry(QtCore.QRect(0, 0, 611, 71))
        self.song_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.song_title.setFont(font)
        self.song_title.setAlignment(QtCore.Qt.AlignCenter)
        self.song_title.setObjectName("song_title")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(150, 140, 300, 300))
        self.graphicsView.setMinimumSize(QtCore.QSize(300, 300))
        self.graphicsView.setMaximumSize(QtCore.QSize(300, 300))
        self.graphicsView.setStyleSheet("border-radius: 150px;\n"
                                        "background-image: url(./images/no game no life.png);pix")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphicsView.setObjectName("graphicsView")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(70, 540, 491, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "bilibiliPlayer"))
        self.song_title.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "选择歌单"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))
# import main_window_rc