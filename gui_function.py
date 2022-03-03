# from function import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem

import function  # 防止from xxx import * 死锁

# res_path = "C:/Users/19147/PycharmProjects/bilibiliPlayer/resources/images/"
play_flag = 0   # 用来解决播放按钮的切换问题


def static_vars(**kwargs):  # 这个装饰器用来产生静态变量（虽然原理没太看懂
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


def gui_switch_song(window, string):
    global play_flag
    temp_cmd = ['play', string]
    function.start_flag = True
    play_flag = 0  # 正在播放
    function.play_song(temp_cmd)
    window.song_title.setText(function.cur_song[0: -4])
    swap_icon(play_flag, window)


def gui_play_song(window):
    global play_flag
    if not function.start_flag:
        function.start_flag = True
        function.play_song(['play'])
    else:
        play_flag = not play_flag
        if play_flag:
            function.pause()
        else:
            function.unpause()
    window.song_title.setText(function.cur_song[0: -4]) # 因为文件最后一定是.mp3,所以去掉4个字符
    swap_icon(play_flag, window)


def gui_next(window):  # 传一个window用于设置标题
    global play_flag
    function.next_song()
    window.song_title.setText(function.cur_song[0: -4])
    play_flag = 0
    swap_icon(0, window)


def gui_previous(window):
    global play_flag
    function.previous_song()
    window.song_title.setText(function.cur_song[0: -4])
    play_flag = 0
    swap_icon(0, window)


def swap_icon(flag, window):
    res_path = function.res_path

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(res_path + "start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    if flag:
        window.play_button.setIcon(icon)
        window.play_button.setIconSize(QtCore.QSize(30, 30))
    else:
        icon.addPixmap(QtGui.QPixmap(res_path + "stop.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)  # play和pause图标是指下一个状态是play还是pause...
        window.play_button.setIcon(icon)
        window.play_button.setIconSize(QtCore.QSize(30, 30))


def gui_search(string):
    temp_cmd = ['search', string]
    return function.search(temp_cmd)


def gui_add_song(av, name):  # 参数是BV号或者av号
    temp_cmd = ['add', av, name]
    print(temp_cmd)
    function.add_song(temp_cmd)


@static_vars(mode=0)
def gui_chmod(window):
    res_path = function.res_path
    icon = QtGui.QIcon()
    gui_chmod.mode = (gui_chmod.mode + 1) % 3
    if gui_chmod.mode == 1:
        function.change_mod(['chmod', 'sequence'])
        icon.addPixmap(QtGui.QPixmap(res_path + "cycle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    elif gui_chmod.mode == 2:
        function.change_mod(['chmod', 'loop'])
        icon.addPixmap(QtGui.QPixmap(res_path + "cycle_one.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    elif gui_chmod.mode == 0:
        function.change_mod(['chmod', 'random'])
        icon.addPixmap(QtGui.QPixmap(res_path + "random.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    window.play_mode_button.setIcon(icon)
    window.play_mode_button.setIconSize(QtCore.QSize(30, 30))


@static_vars(flag=0)
def gui_play_list(window):
    song_list = function.print_list(['ls'])
    gui_play_list.flag = not gui_play_list.flag

    if gui_play_list.flag:
        for index, song in enumerate(song_list):
            window.song_list_page.tableWidget.insertRow(index)
            window.song_list_page.tableWidget.setItem(index, 0, QTableWidgetItem(song))
        window.song_list_page.show()
    else:
        window.song_list_page.tableWidget.clear()
        window.song_list_page.tableWidget.setRowCount(0)
        window.song_list_page.hide()


def set_widget_icon(widget, path):  # 给具体的控件设置icon
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal,
                   QtGui.QIcon.Off)
    widget.setIcon(icon)
    widget.setIconSize(QtCore.QSize(30, 30))
