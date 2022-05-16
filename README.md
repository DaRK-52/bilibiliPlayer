# bilibiliPlayer

## 简介
bilibiliPlayer是一款将b站上的视频转换为音频保存在本地并进行播放的音乐播放器。

## 使用方式
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