from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow
from main_window import *
from gui_function import *
from search_window import *

res_path = 'C:/Users/19147/PycharmProjects/bilibiliPlayer'


class search_window(QMainWindow, Ui_SearchWindow):
    def __init__(self, parent=None):
        super(search_window, self).__init__(parent)
        self.setupUi(self)
        self.table_row_num = 0 # 表格的行数
        self.tableWidget.doubleClicked.connect(self.add_song)
        self.setFixedSize(600, 800)

    def add_song(self):
        av = self.tableWidget.selectedItems()[1].text()    # 获取av号或者bv号
        name = self.SearchEdit.text()   # 先不支持自定义文件名，直接拿搜索的字段命名
        gui_add_song(av, name)

    def search(self, string):
        title_list, v_list = gui_search(string)
        self.update_table(title_list, v_list)

    def update_table(self, list1, list2):
        self.tableWidget.clear()
        while self.table_row_num < len(list1):
            self.tableWidget.insertRow(self.table_row_num)

            self.tableWidget.setItem(self.table_row_num, 0, QTableWidgetItem(list1[self.table_row_num]))
            self.tableWidget.setItem(self.table_row_num, 1, QTableWidgetItem(list2[self.table_row_num]))
            self.table_row_num = self.table_row_num + 1

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Enter - 1:
            self.search(self.SearchEdit.text())
            pass


class my_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(my_window, self).__init__(parent)
        self.setupUi(self)
        self.search_page = search_window()
        self.search_page.tableWidget.setColumnWidth(0, 380)
        self.search_page.tableWidget.setColumnWidth(1, 125)
        self.page = "main"
        self.configure_button()
        self.setIcon()
        self.setFixedSize(600, 800)

    def configure_button(self):  # 配置button
        self.play_button.clicked.connect(lambda: gui_play_song(self))
        self.next_button.clicked.connect(lambda: gui_next(self))
        self.previous_button.clicked.connect(lambda: gui_previous(self))
        self.change_page_button.clicked.connect(self.change_page)
        self.search_page.change_page_button.clicked.connect(self.change_page)

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

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(res_path + "/images/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_page_button.setIcon(icon6)
        self.change_page_button.setIconSize(QtCore.QSize(30, 30))
        self.change_page_button.setFlat(True)
        self.search_page.change_page_button.setIcon(icon6)
        self.search_page.change_page_button.setIconSize(QtCore.QSize(30, 30))
        self.search_page.change_page_button.setFlat(True)

    def change_page(self):
        if self.page == "main":
            self.search_page.show()
            self.hide()
            self.page = "search"
        else:
            self.search_page.hide()
            self.search_page.tableWidget.clear()    # 清除搜索结果
            self.search_page.SearchEdit.clear() # 清除搜索内容
            self.search_page.table_row_num = 0
            self.show()
            self.page = "main"

    def closeEvent(self, event):
        pass
