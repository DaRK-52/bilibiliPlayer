from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow

import gui_function
from main_window import *
from new_main_window import *
from gui_function import *
from search_window import *
from song_list_window import *


class search_window(QMainWindow, Ui_SearchWindow):
    def __init__(self, parent=None):
        super(search_window, self).__init__(parent)
        self.main_w = None  # 因为需要进行window的切换，所以这个对象里面也要存main_window的对象
        self.setupUi(self)
        self.set_icon()
        self.configure_button()

        self.table_row_num = 0  # 表格的行数
        self.tableWidget.doubleClicked.connect(self.add_song)

        self.setGeometry(1200, 180, 360, 600)
        self.setFixedSize(360, 600)

    def configure_button(self):
        self.change_page_button.clicked.connect(self.change_page)

    def set_icon(self):
        res_path = function.res_path
        self.disc_3.setPixmap(QtGui.QPixmap(res_path + "disc.png"))
        set_widget_icon(self.change_page_button, res_path + "add_to_list.png")
        self.change_page_button.setFlat(True)

    def set_main(self, main_w):
        self.main_w = main_w

    def add_song(self):
        av = self.tableWidget.selectedItems()[1].text()  # 获取av号或者bv号
        name = self.SearchEdit.text()  # 先不支持自定义文件名，直接拿搜索的字段命名
        gui_add_song(av, name)

    def search(self, string):
        title_list, v_list = gui_search(string)
        self.update_table(title_list, v_list)

    def update_table(self, list1, list2):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.table_row_num = 0
        while self.table_row_num < len(list1):
            self.tableWidget.insertRow(self.table_row_num)

            self.tableWidget.setItem(self.table_row_num, 0, QTableWidgetItem(list1[self.table_row_num]))
            self.tableWidget.setItem(self.table_row_num, 1, QTableWidgetItem(list2[self.table_row_num]))
            self.table_row_num = self.table_row_num + 1

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Enter - 1:
            self.search(self.SearchEdit.text())
            pass

    def change_page(self):
        self.hide()
        self.tableWidget.clear()  # 清除搜索结果
        self.SearchEdit.clear()  # 清除搜索内容
        self.tableWidget.setRowCount(0)
        self.table_row_num = 0
        self.main_w.show()


class song_list_window(QMainWindow, Ui_SongListWindow):
    def __init__(self, parent=None):
        super(song_list_window, self).__init__(parent)
        self.main_w = None
        self.setupUi(self)
        self.setGeometry(1200, 380, self.width(), self.height())
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.tableWidget.doubleClicked.connect(lambda: self.play(self.tableWidget.selectedItems()[0].text()))

    def set_main(self, main_w):
        self.main_w = main_w

    def play(self, string):
        gui_switch_song(self.main_w, string)


class my_window(QMainWindow, Ui_New_MainWindow):
    def __init__(self, parent=None):
        super(my_window, self).__init__(parent)
        self.setupUi(self)
        self.search_page = search_window()
        self.search_page.set_main(self)
        self.search_page.tableWidget.setColumnWidth(0, 380)
        self.search_page.tableWidget.setColumnWidth(1, 125)

        self.song_list_page = song_list_window()
        self.song_list_page.set_main(self)

        self.configure_button()
        self.set_icon()
        self.setGeometry(800, 600, 400, 180);
        self.setFixedSize(400, 180)

    def configure_button(self):  # 配置button
        self.play_mode_button.clicked.connect(lambda: gui_chmod(self))
        self.play_button.clicked.connect(lambda: gui_play_song(self))
        self.next_button.clicked.connect(lambda: gui_next(self))
        self.previous_button.clicked.connect(lambda: gui_previous(self))
        self.play_table_song_button.clicked.connect(lambda: gui_play_list(self))
        self.change_page_button.clicked.connect(self.change_page)

    def set_icon(self):
        res_path = function.res_path
        # 设置应用图标
        self.disc_3.setPixmap(QtGui.QPixmap(res_path + "disc.png"))

        set_widget_icon(self.play_mode_button, res_path + "random.png")

        set_widget_icon(self.previous_button, res_path + "on.png")

        set_widget_icon(self.play_button, res_path + "start.png")

        set_widget_icon(self.next_button, res_path + "de.png")

        set_widget_icon(self.play_table_song_button, res_path + "open_folder.png")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(res_path + "disc1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        set_widget_icon(self.change_page_button, res_path + "add_to_list.png")
        self.change_page_button.setFlat(True)

    def change_page(self):
        self.search_page.show()
        self.hide()

    def closeEvent(self, event):
        pass
