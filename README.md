# bilibiliPlayer
bilibili音频播放器

通过you-get下载b站的视频并转成mp3存储

提供一个CLI的播放器，也支持GUI界面

首先安装requirements.txt下的库，接着在resources/settings.txt下修改环境配置，然后python main.py即可

基本命令：

**gui**     // 进入图形化界面

add BVxxx yyy // 下载BV号为xxx的视频，存储为yyy.mp3

play xxx  // 播放xxx.mp3

next  //播放下一首

pause

unpause

ps  // 显示当前播放歌曲

chmod // 更改播放方式（循环，顺序，随机）

search xxx // 在b站搜索xxx,会返回一个带视频标题和BV号的列表，选择序号下载想要的
