# bilibiliPlayer

## 简介
bilibiliPlayer是一款将b站上的视频转换为音频保存在本地并进行播放的音乐播放器。开发目的是为了解决想听的许多音乐需要在不同音乐播放软件下开会员才能听，以及一些b站特有的二创鬼畜在主流音乐软件下并没有发布的问题。

这也是我IS305应用软件课程设计的小作业。

## 开始运行
**安装相关依赖**
> pip install -r requirements.txt

**clone项目到本地**
> git clone https://github.com/DaRK-52/bilibiliPlayer.git

**修改配置文件**

修改bilibiliPlayer/resources文件夹下的settings.json文件。
- audio_path是您希望保存音频的位置
- src_path是保存歌单信息的位置
- res_path是图形化界面中图片资源的位置，通常就是bilibiliPlayer/resources/images的绝对路径

**运行程序**
> cd bilibiliPlayer

> python main.py

如上即可运行程序，具体程序使用方式如下所示。

## 使用方式
程序提供CLI和GUI两种方式，CLI下的运行命令如下所示：

| 命令   | 命令意义   |
| --- | --- |
|  help   |  输出帮助文档   |
|  add    |  添加歌曲，支持通过av号和BV号添加     |
|  ls     |  输出当前所有的歌曲     |
|  play   |  播放歌曲      |
|  chmod  |  更改播放模式，支持随机，顺序，循环三种模式     |
|  pause | 暂停播放  |
|  unpause | 取消暂停  |
|  next |  播放下一首歌曲 |
|  previous | 播放上一首歌曲（如果历史歌单为空则会停止播放）  |
|  ps | 显示当前运行状态  |
|  export | 修改audio_path,src_path和res_path的值  |
|  ps | 显示当前歌曲运行状态，包括播放模式和当前正在播放哪首歌曲  |
|  search | 搜索歌曲，会返回一个列表，在其中输入编号选择您想下载的歌曲  |
|  gui | 启动图形化界面  |
|  exit | 退出程序  |


| 不推荐使用的命令   | 命令意义   |
| --- | --- |
| use  | 选取某个歌单  |
| create  | 创建歌单  |
| desc  |  显示歌单信息 |
| update  | 向歌单中加入或删除歌曲  |

GUI的使用方式属于是点开就能会用，在命令行中输入gui启动图形化界面

![](https://notes.sjtu.edu.cn/uploads/upload_fff9250de33bca8af8d4f30ebad03ae3.png)

下方按钮从左到右分别是更改播放模式，上一首歌曲，暂停，下一首歌曲和打开歌单查看，歌单如下所示

![](https://notes.sjtu.edu.cn/uploads/upload_e1cad63a99735d842ae325dc4eb371af.png)

再次点击按钮可以关闭歌单

点击右上角按钮可以进入搜索栏，输入想听的歌会返回搜索结果，双击下载您想要的歌曲。
![](https://notes.sjtu.edu.cn/uploads/upload_8b5609a5f311d0ab6fd0faac20f29559.png)

再次点击可以回到主界面

## BUG&Feature
- 由于线程同步当中的逻辑问题，第一首歌的播放有概率会出错
- CLI命令的设计参考了mysql和linux基本命令，但mysql这块的命令又没设计好，和原来的mysql命令不太一样，所以不推荐使用歌单功能

## 进一步修改
您可以修改这个程序使它支持youtube或是其他一些视频网站，最少只需要修改function.py中的add_song函数。