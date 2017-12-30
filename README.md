

> 全世界 JavaScript 开发者团结起来!

一个帮助「跳一跳」玩家打榜的小工具

[![node](https://img.shields.io/node/v/passport.svg)]()
[![npm](https://img.shields.io/npm/v/npm.svg)]()

yarn v1.3.2

express 4.15.5

nodemon 1.14.5

## 准备工作

- Mac / Linux 环境

- 配置好 node 和 node 下载源[参考](https://npm.taobao.org/)

- Android 手机(正常的就行，不要刷开发版)

- 在电脑上安装 adb [adb 参考](https://www.jianshu.com/p/5ba1cf5869bc)

- 测试: 安装完 adb, 确保 adb 在你的环境路径中。打开终端执行 `adb shell input keyevent 3` 观察是否会回到首屏(即按下 Home 键的效果)。如果可以返回首屏则此手机可以使用。

## 运行方法

0. 手机连接电脑并打开 `usb 调试`

1. 运行 `git clone `

2. 运行 `cd wxgame-jump-helper && npm install`

    Yarn 党: `cd wxgame-jump-helper && yarn`

3. 运行 `nodemon`

4. 在浏览器中打开 [http://localhost:3000/jump](http://localhost:3000/jump) 看到如图示界面: 

[首次打开][firstScreen]

5. 如果一切正常，打开微信小游戏跳一跳, 点击开始游戏。

6. 随后在浏览器图片内同一位置点击两次，等待一会儿会载入手机显示的画面。

7. 先点击小人所在位置，再点击要跳到的位置，如果参数配置正确，稍等几秒就可以看到得分画面。

[得分画面][secondScreen]

## 参数调整

因为手机型号和分辨率不同，默认的参数无法适用你的手机是正常的。暂时需要手动调节参数，具体方法如下:

1. 将 `views/jump.jade` 中 `jumpAction` 函数里的 `needAdjust` 设置为 `true` 。

2. 重新按照运行方法提示进行。

3. 每次实验结果会保存在 `output.txt` 中，请及时移除失败的记录否则可能干扰参数结果。

4. 调整参数需要本地安装 python 环境并安装 `matplotlib numpy scipy` 。具体可以通过 `pip install -r requirements.txt` 完成。

5. 参数计算方法参考[链接](https://www.cnblogs.com/NanShan2016/p/5493429.html)。在项目目录下运行 `python get_args.py` 获得如图示结果:

[调参][adjustArgs]

6. 复制 `k`, `b` 的值到 `views/jump.jade` 中 `jumpAction` 函数里，并将 needAdjust 恢复为 false

7. 你已经调整好适用于自己手机的参数，现在能阻止得分的只有你的心情。

**Happy Playing !!!**

## TODO

- 历史回放
- 自动读取距离 canvas (canvas.getImages) 注意背景会变化
- js 实现最小二乘法拟合
- iphone
- mac -> linux/win
- js嵌入式做物理外挂
- realtime 反馈调节 websocket
- 产生的训练集调整 js 代码参数
- 去除偏差较大的实验组
- 定时清理截图
- python 调参 云端环境

### 其他

关于这个项目的更多介绍，可以关注下方公众号发送 “jump”。

![微信公众号][微信公众号]

如果觉得这个项目对你有帮助，可以帮忙多多宣传。

如果你有任何想法可以和我交流。微信号: gitbear [知乎](https://www.zhihu.com/people/gitbear/)

[firstScreen]: src/0.jpg
[secondScreen]: src/1.jpg
[adjustArgs]: src/2.
[微信公众号]: src/sub.jpg