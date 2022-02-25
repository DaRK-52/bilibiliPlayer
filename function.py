import os
import time
import re
import requests
import win32con
import win32api
import threading
import pickle
import joblib
import pygame
import random
from str2byte import *

RANDOM = 0
SEQUENCE = 1
LOOP = 2  # 随机，列表，循环三种播放模式
mod_dict = {'random': RANDOM, 'sequence': SEQUENCE, 'loop': LOOP}
cmd_list = {'exit', 'play', 'add', 'next', 'ls', 'pause', 'unpause', 'help', 'chmod', 'ps', 'search', 'export',
            'create', 'update', 'use', 'desc'}

audio_path = "E:/bilibiliPlayer/audio/"  # 建议修改为自己的路径，也可以使用export命令修改
src_path = "E:/bilibiliPlayer/src_list/"

# 其中的local歌单是当前目录下的所有歌曲
song_table = {}  # 存放歌单相关信息，会把它序列化
cur_song_table = '' # 记录当前播放的歌单名
# song_table_list = {}  # 存放每个歌单中的歌曲

play_mode = RANDOM  # 默认随机播放
song_list = []  # 待播放歌曲列表
song_num = 0  # 歌曲数量
cur_song = -1  # 正在播放的歌曲， 防止随机播放播放出同一首哥
start_flag = False
close_flag = False  # 关闭标识，用于结束监听线程


def print_help():
    f = open(src_path + "readme.txt", encoding="utf-8")
    text = f.readlines()
    for line in text:
        print(line, end='')  # 自带换行符，最后不换行
    f.close()


def print_list(cmd):    # 支持查看歌单里面的内容
    global song_list, song_table
    if len(cmd) == 1:
        for song in song_list:
            print(str(song_list.index(song)) + ": " + song)
    else:
        cmd_song_table = cmd[1] # 想来想去觉得还是不要有空格比较好
        if cmd_song_table in song_table.keys():
            for song in song_table[cmd_song_table]:
                print(str(song_table[cmd_song_table].index(song)) + ": " + song)
        else:
            print("歌单" + cmd_song_table + "不存在！")


def merge_name(cmd):
    ret = ""
    for i in range(0, len(cmd) - 1):
        ret += cmd[i] + " "
    ret += cmd[len(cmd) - 1]
    return ret


#   检查下载的时候BV号是否存在
def check_BV_not_exist(song):
    res = requests.get("https://www.bilibili.com/video/" + song)
    if ("very_sorry.png" in res.text):  # 判断BV号是否存在，利用页面上是否有very_sorry.png判断
        return True
    return False


def check_name_not_exist(name):  # 检查歌曲名是否已经存在
    if os.path.exists(audio_path + name + ".mp3") or os.path.exists(
            audio_path + name[0:-1] + ".mp3"):
        return True
    return False


def add_song(cmd):
    song = cmd[1]  # 获取歌曲对应BV号

    if check_BV_not_exist(song):
        print("BV号不存在")
        return

    if len(cmd) == 2:
        name = song  # 歌曲默认名字为BV号
    else:
        name = merge_name(cmd[2:])  # 将名字中的空格以下划线代替后拼接起来

    if check_name_not_exist(name):  # 判断有无重复歌曲名
        print("名称已存在，请重命名")
        return

    os.system("you-get https://www.bilibili.com/video/" + song + " -O \"" + audio_path + "temp\"")
    os.system("ffmpeg -i E:/bilibiliPlayer/audio/temp.mp4 -vn \"" + audio_path + name + ".mp3\"")
    os.system("del/f/s/q temp.mp4")  # 下载视频， 转换成音频文件，删除temp文件
    os.system("del/f/s/q *.xml")  # 删除弹幕文件，由于当前目录在audio_path下，所以直接删除当前目录的xml文件就行
    update_list()  # 更新歌曲列表


def check_song_not_exist(song):
    for i in song_list:
        if i == song:
            return False
    return True


def pygame_play_song(path, file):
    global cur_song
    cur_song = file
    pygame.mixer.music.load(path + file)
    pygame.mixer.music.play()


def play_song(cmd):
    global cur_song
    if len(cmd) == 1:
        # 默认播放第一首歌曲
        pygame_play_song(audio_path, song_list[0])
        return 0
    else:
        try:
            x = int(cmd[1])
            if x < 0 or x >= song_num:
                print("Out of bounds of song_list\n")
                return 1  # 1代表错误， 0代表无错误
            pygame_play_song(audio_path, song_list[x])
            return 0
        except ValueError:
            pass

        if check_song_not_exist(cmd[1] + ".mp3") and check_name_not_exist(cmd[1]):
            print("歌曲" + cmd[1] + "不存在\n")
            return 1
        if ".mp3" not in cmd[1]:
            pygame_play_song(audio_path, cmd[1] + ".mp3")
        else:
            pygame_play_song(audio_path, cmd[1])
        return 0


def not_cmd(cmd):
    if cmd in cmd_list:
        return False
    return True


def get_another_song():  # 防止在随机播放时连续播放同一首歌
    while True:
        random.seed(time.time())  # 不知道有没有用
        x = random.randint(0, song_num - 1)
        if song_list[x] != cur_song:
            break
    return x


def listener():  # 监听歌曲是否结束，如果结束就切下一首歌
    temp_cmd = ['play']
    pygame.mixer.init()
    while True:
        if (pygame.mixer.music.get_busy() or start_flag is False) and not close_flag:  # 还未开始或正在播放
            time.sleep(0.1)
        else:
            if close_flag:  # 判断程序是否结束
                break
            next_song()


def next_song():
    temp_cmd = ['play']
    if play_mode == LOOP:
        # print("You are in loop mode, next song will still be the same")
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


def update_local_list():
    song_table['local'] = []
    for i in os.listdir(audio_path):
        song_table['local'].append(i)
    update_song_table()  # 仅加入local歌单


def update_list():  # 需要重新修改
    global song_list
    global song_num
    # song_list = os.listdir(audio_path)  # 刷新获取当前目录下的歌曲
    # song_num = len(song_list)
    # song_table['local'] = []
    # for i in os.listdir(audio_path):
    #     song_table['local'].append(i)
    # update_song_table()     # 仅加入local歌单
    update_local_list()


def load_song_table():
    global song_table
    f = open(src_path + 'list.txt', 'rb')
    if os.path.getsize(src_path + 'list.txt') > 0:
        song_table = pickle.load(f)
    f.close()


#   初始化设置
def init():
    global play_mode, song_table
    global cur_song_table, song_list
    play_mode = RANDOM  # 默认播放方式为随机
    random.seed(time.time())
    load_song_table()  # 先加载歌单

    update_list()  # 更新曲目

    temp_cmd = ['use', 'local']
    cur_song_table = 'local'
    use_song_table(temp_cmd)  # 默认使用local歌单

    pygame.mixer.init()

    if 'local' not in song_table.keys():
        update_local_list()


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


# 这个命令似乎线程危险，如果在一首歌即将结束的时候调用这个命令，它有可能会返回上一首歌
def ps(cmd):
    print("当前播放方式:" + list(mod_dict.keys())[
        list(mod_dict.values()).index(play_mode)])  # 逆天通过值反查键，不过由于键值一一对应所以也没什么关系
    if cur_song != -1:
        print("当前播放歌曲:" + cur_song)
    else:
        print("当前无播放歌曲")
    print("当前歌单：" + cur_song_table)


def get_search_text(cmd):
    text = ''
    cmd_iterator = iter(cmd)
    next(cmd_iterator)  # 跳过第一个元素
    while True:
        try:
            text = text + next(cmd_iterator) + "%20"
        except StopIteration:
            break
    text = text[0:-3]  # 去除最后一个%20
    return text


# search需要重新修改以支持av号搜索
def search(cmd):
    if len(cmd) == 1:
        print("请输入您想要搜索的内容\n")
        return

    search_text = get_search_text(cmd)

    r = requests.get("https://search.bilibili.com/all?keyword=" + search_text)
    result = re.findall(r'<a title=.*href="//www.bilibili.com/video/BV[A-Za-z0-9]+', r.text)  # 奇妙的正则匹配

    title_list = []
    BV_list = []
    for i, info in enumerate(result):
        tmp = info.split("\"")
        title_list.append(tmp[1])  # 纯纯的正则表达式匹配，匹配下来的第一个项是title所以它一定会夹在第一个"和第二个"间
        BV_list.append(re.findall(r'BV[a-zA-Z0-9]+', info)[0])  # 将BV号加入列表
        print(str(i) + " title:" + tmp[1] + " " + re.findall(r'BV[a-zA-Z0-9]+', info)[0])
    print('请选择您想下载的音乐（输入序号与歌曲名即可（无歌曲名默认为BV号）,若无输入back即可）')

    select_cmd = input()
    select_cmd = select_cmd.split(' ')
    if select_cmd[0] == 'back':
        return
    try:
        if int(select_cmd[0]) > len(title_list):  # 这里理论上需要一个catch
            print('没有那么多歌曲')
            return
    except ValueError:
        print("请输入序号")
        return

    if len(select_cmd) == 1:
        temp_cmd = ['add', BV_list[int(select_cmd[0])], BV_list[int(select_cmd[0])]]
    else:
        temp_cmd = ['add', BV_list[int(select_cmd[0])], merge_name(select_cmd[1:])]
    add_song(temp_cmd)


def export_path(cmd):
    global audio_path
    if len(cmd) == 1:
        print("需要更多参数")
        return
    audio_path = cmd[1]


def create(cmd):
    if len(cmd) < 3:
        print("需要更多参数")
        return

    if cmd[1] == 'table':   # 这里其实是想保留创建更多其他结构的可能，但可能没有了
        list_name = merge_name(cmd[2:])
        if list_name in song_table.keys():
            print("歌单名重复，请重新考虑歌单名")
            return
        song_table[list_name] = []  # 创建一个空歌单
        f = open(src_path + "list.txt", "wb")
        pickle.dump(song_table, StrToBytes(f), 1)  # 二进制存储
        f.close()


def update_song_table():  # 序列化写入
    global song_table
    f = open(src_path + "list.txt", "wb")
    pickle.dump(song_table, StrToBytes(f), 1)
    f.close()


def update(cmd):
    global song_table
    if len(cmd) < 4:
        print("需要更多参数")
        return

    if cmd[1] not in song_table.keys():
        print("不存在这个歌单")
        return

    if cmd[2] not in ('add', 'drop'):
        print("不存在指令" + cmd[2])
        return

    if cmd[3] not in song_list:
        try:  # 尝试支持通过序号添加歌单歌曲
            x = int(cmd[3])  # 只支持通过local歌单的列表来添加
            if 0 <= x < len(song_table['local']):
                value = song_table['local'][x]
            else:
                value = int('asdasdasd')    # 强行触发ValueError
                print(value)
        except ValueError:
            print("不存在歌曲" + cmd[3])
            return
    else:
        value = cmd[3]

    key = cmd[1]
    command = cmd[2]

    # print(type(song_table[key]))
    if command == 'add':
        song_table[key].append(value)

    update_song_table()
    use_song_table(['use', cur_song_table]) # 更新当前歌单，防止ls出问题
    # f = open(src_path + "list.txt", "wb")
    # pickle.dump(song_table, StrToBytes(f), 1)
    # f.close()


def use_song_table(cmd):
    global song_list, song_table
    global song_num, cur_song_table
    if len(cmd) < 2:
        print("需要更多参数")
        return

    if cmd[1] not in song_table.keys():
        print("不存在歌单" + cmd[1])
        return

    cur_song_table = cmd[1]
    song_list = []
    for value in song_table[cmd[1]]:
        song_list.append(value)
    song_num = len(song_list)  # 替换为我们选择的歌单


def desc(cmd):  # 显示歌单信息
    for i in song_table.keys():
        print(str(list(song_table.keys()).index(i)) + ":" + i)
