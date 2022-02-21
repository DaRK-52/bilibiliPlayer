import os
import time

import requests
import win32con
import win32api
import threading
import pygame
import random

RANDOM = 0
SEQUENCE = 1
LOOP = 2  # 随机，列表，循环三种播放模式
mod_dict = {'random': RANDOM, 'sequence': SEQUENCE, 'loop': LOOP}
cmd_list = {'exit', 'play', 'add', 'next', 'ls', 'pause', 'unpause', 'help', 'clear', 'chmod'}

audio_path = "E:/bilibiliPlayer/audio/"
src_path = "E:/bilibiliPlayer/src_list/"
play_mode = RANDOM  # 默认随机播放
song_list = []  # 待播放歌曲列表
song_num = 0  # 歌曲数量
cur_song = -1  # 正在播放的歌曲， 防止随机播放播放出同一首哥
start_flag = False
close_flag = False  # 关闭标识，用于结束监听线程


def print_help():
    f = open(src_path + "readme.txt")
    text = f.readlines()
    print(text)
    f.close()


def merge_name(cmd):
    ret = ""
    for i in range(2, len(cmd) - 1):
        ret += cmd[i] + "_"
    ret += cmd[len(cmd) - 1]
    return ret


#   检查下载的时候BV号是否存在
def check_BV_not_exist(song):
    res = requests.get("https://www.bilibili.com/video/" + song)
    if ("very_sorry.png" in res.text):  # 判断BV号是否存在，利用页面上是否有very_sorry.png判断
        return True
    return False


def add_song(cmd):
    song = cmd[1]

    if check_BV_not_exist(song):
        print("BV号不存在")
        return

    if len(cmd) == 2:
        name = song
    else:
        name = merge_name(cmd)

    if os.path.exists("E:/bilibiliPlayer/audio/" + name + ".mp4") or os.path.exists(
            "E:/bilibiliPlayer/audio/" + name[0:-1] + ".mp4"):
        print("名称已存在，请重命名")
        return

    os.system("you-get https://www.bilibili.com/video/" + song + " -O E:/bilibiliPlayer/audio/temp")
    os.system("ffmpeg -i E:/bilibiliPlayer/audio/temp.mp4 -vn E:/bilibiliPlayer/audio/" + name + ".mp3")
    os.system("del/f/s/q E:\\bilibiliPlayer\\audio\\temp.mp4")  # 下载视频， 转换成音频文件，删除temp文件
    print(audio_path + "*.xml")
    # os.system("del/f/s/q " + audio_path + "/*.xml")     # 删除弹幕文件
    os.system("del/f/s/q *.xml")    # 删除弹幕文件，由于当前目录在audio_path下，所以直接删除当前目录的xml文件就行
    update_list()  # 更新歌曲列表


def check_song_not_exist(song):
    for i in song_list:
        if i == song:
            return False
    return True


def play_song(cmd):
    global cur_song
    if len(cmd) == 1:
        cur_song = song_list[0] # 默认播放第一首歌曲
        pygame.mixer.music.load(audio_path + song_list[0])
        pygame.mixer.music.play()
    else:
        try:
            x = int(cmd[1])
            if x < 0 or x >= song_num:
                print("Out of bounds of song_list\n")
                return
            pygame.mixer.music.load(audio_path + song_list[x])
            pygame.mixer.music.play()
            return
        except ValueError:
            pass
        if check_song_not_exist(cmd[1]):
            print("歌曲" + cmd[1] + "不存在\n")
            return
        cur_song = cmd[1]
        pygame.mixer.music.load(audio_path + cmd[1])
        pygame.mixer.music.play()


def not_cmd(cmd):
    if cmd in cmd_list:
        return False
    return True


def get_another_song():
    while True:
        x = random.randint(0, song_num - 1)
        if song_list[x] != cur_song:
            break
    return x


def listener():
    temp_cmd = ['play']
    while True:
        if (pygame.mixer.music.get_busy() or start_flag is False) and not close_flag:  # 还未开始或正在播放
            time.sleep(0.1)
        else:
            if close_flag:  # 判断程序是否结束
                break
            next_song()
            # x = get_another_song()
            # temp_cmd.append(song_list[x])
            # play_song(temp_cmd)


def next_song():
    temp_cmd = ['play']
    if play_mode == LOOP:
        print("You are in loop mode, next song will still be the same")
        temp_cmd.append(cur_song)
        play_song(temp_cmd)
    elif play_mode == RANDOM:
        x = get_another_song()
        temp_cmd.append(song_list[x])
        play_song(temp_cmd)
    elif play_mode == SEQUENCE:
        x = song_list.index(cur_song)  # 获取当前正在播放的歌曲序号
        x = x + 1  # 切换到下一首
        temp_cmd.append(song_list[x])
        play_song(temp_cmd)


def update_list():
    global song_list
    global song_num
    song_list = os.listdir(audio_path)
    song_num = len(song_list)


#   初始化设置
def init():
    global play_mode
    play_mode = RANDOM
    update_list()  # 更新曲目
    pygame.mixer.init()


def change_mod(cmd):
    global play_mode
    if len(cmd) == 1:
        print("Need more arguments, play_mod can be random, sequence or loop")
        return
    mod = cmd[1].lower()
    if mod not in ['sequence', 'random', 'loop']:
        print("Need correct mod, play_mod can be random, sequence or loop")
        return
    play_mode = mod_dict[mod]


if __name__ == "__main__":
    print("Welcome to use bilibiliPlayer\n")
    init()

    listener_thread = threading.Thread(target=listener, args=())
    listener_thread.start()
    os.chdir(audio_path)
    # print("current working directory is " + os.getcwd() + "\n")

    while True:
        raw_cmd = input("")
        raw_cmd = raw_cmd.strip()
        cmd = raw_cmd.split(" ")

        # 待解决：如何解决多个if的问题，是否能用类似switch的方式解决
        if cmd[0] == "exit":
            close_flag = True
            break

        if cmd[0] == "add":
            add_song(cmd)

        if cmd[0] == "help":
            print_help()

        if cmd[0] == "play":
            if len(cmd) == 1 and start_flag is True:
                print("Player is running\n")
                continue

            start_flag = True
            play_song(cmd)

        if cmd[0] == "next":
            next_song()

        if cmd[0] == "ls":
            for song in song_list:
                print(str(song_list.index(song)) + ": " + song)

        if cmd[0] == "pause":
            pygame.mixer.music.pause()

        if cmd[0] == "unpause":
            pygame.mixer.music.unpause()

        if cmd[0] == "clear":
            os.system("cls")

        if cmd[0] == "chmod":  # 更改播放模式
            change_mod(cmd)

        if not_cmd(cmd[0]):
            print("Exec " + cmd[0] + " Failed.Please check your command.")

    print("Bye\n")
    pygame.mixer.quit()
    pygame.quit()