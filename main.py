import os
import time

import requests
import win32con
import win32api
import threading
import pygame
import random
import function
from function import *
from window import *

if __name__ == "__main__":
    print("Welcome to use bilibiliPlayer")
    init()  # 初始化设置
    listener_thread = threading.Thread(target=listener, args=())
    listener_thread.start()  # 开启监听线程

    os.chdir(audio_path)  # 切换到保存音频的目录下

    while True:
        raw_cmd = input("$ ")
        raw_cmd = raw_cmd.strip()
        cmd = raw_cmd.split(" ")

        # 待解决：如何解决多个if的问题，是否能用类似switch的方式解决
        # 能否直接通过搜索关键词找到BV号
        # 下载封面功能
        # 增加分组功能，类似于分歌单
        # GUI
        # 急需重写随机功能，random模式每次顺序都一样
        if cmd[0] == "exit":
            function.close_flag = True  # 设置close_flag为true，使监听线程退出
            break

        if cmd[0] == "add":
            add_song(cmd)  # 添加歌曲

        if cmd[0] == "help":
            print_help()  # 输出帮助

        if cmd[0] == "play":
            if len(cmd) == 1 and function.start_flag is True:
                print("Player is running")
                continue

            status = play_song(cmd)
            if not status:
                function.start_flag = True

        if cmd[0] == "next":
            next_song()

        if cmd[0] == "ls":
            print_list()

        if cmd[0] == "pause":
            pygame.mixer.music.pause()

        if cmd[0] == "unpause":
            pygame.mixer.music.unpause()

        if cmd[0] == "chmod":  # 更改播放模式
            change_mod(cmd)

        if cmd[0] == "ps":  # 显示当前运行状态
            ps(cmd)

        if cmd[0] == "search":
            search(cmd)

        if cmd[0] == "export":
            export_path(cmd)    # 修改audio_path

        if not_cmd(cmd[0]):
            print("Exec " + cmd[0] + " Failed.Please check your command.")

    print("Bye")
    pygame.mixer.quit()
    pygame.quit()