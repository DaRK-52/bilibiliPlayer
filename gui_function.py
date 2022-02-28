# from function import *
from PyQt5 import QtGui, QtCore

import function  # 防止from xxx import * 死锁

res_path = 'C:/Users/19147/PycharmProjects/bilibiliPlayer'
play_flag = 0


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


@static_vars()
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
    window.song_title.setText(function.cur_song)
    swap_icon(play_flag, window)


def gui_next(window):  # 传一个window用于设置标题
    global play_flag
    function.next_song()
    window.song_title.setText(function.cur_song)
    play_flag = 0
    swap_icon(0, window)


def gui_previous(window):
    global play_flag
    function.previous_song()
    window.song_title.setText(function.cur_song)
    play_flag = 0
    swap_icon(0, window)


def swap_icon(flag, window):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(res_path + "/images/24gf-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    if flag:
        window.play_button.setIcon(icon)
        window.play_button.setIconSize(QtCore.QSize(30, 30))
    else:
        icon.addPixmap(QtGui.QPixmap(res_path + "/images/24gf-pause2.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)  # play和pause图标是指下一个状态是play还是pause...
        window.play_button.setIcon(icon)
        window.play_button.setIconSize(QtCore.QSize(30, 30))


def gui_search(string):
    temp_cmd = ['search', string]
    return function.search(temp_cmd)


def gui_add_song(av, name):   # 参数是BV号或者av号
    temp_cmd = ['add', av, name]
    print(temp_cmd)
    function.add_song(temp_cmd)