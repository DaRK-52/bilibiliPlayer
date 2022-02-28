from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from main_window import *
from gui_function import *

res_path = 'C:/Users/19147/PycharmProjects/bilibiliPlayer'


class my_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(my_window, self).__init__(parent)
        self.setupUi(self)
        self.configure_button()
        self.setIcon()
        self.setFixedSize(600, 800)

    def configure_button(self):  # 配置button
        self.play_button.clicked.connect(lambda: gui_play_song(self))
        self.next_button.clicked.connect(lambda: gui_next(self))
        self.previous_button.clicked.connect(lambda: gui_previous(self))

    def setIcon(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(res_path + "/images/random.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_mode_button.setIcon(icon)
        self.play_mode_button.setIconSize(QtCore.QSize(30, 30))

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(res_path + "/images/24gf-previousFrame.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_button.setIcon(icon1)
        self.previous_button.setIconSize(QtCore.QSize(30, 30))

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(res_path + "/images/24gf-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon2)
        self.play_button.setIconSize(QtCore.QSize(30, 30))

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(res_path + "/images/24gf-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon3)
        self.next_button.setIconSize(QtCore.QSize(30, 30))

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(res_path + "/images/24gf-playlistMusic4.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.play_table_song_button.setIcon(icon4)
        self.play_table_song_button.setIconSize(QtCore.QSize(30, 30))

        self.graphicsView.setStyleSheet("border-radius: 150px;\n"
                                        "background-image: url(" + res_path + "/images/no game no life.png);pix")

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(res_path + "/images/windowIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon5)

    def closeEvent(self, event):
        pass
