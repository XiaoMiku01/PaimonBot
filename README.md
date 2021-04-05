## 派蒙Bot / PaimonBot
基于[Mrs4s](https://github.com/Mrs4s) / [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 和 [nonebot](https://github.com/nonebot) / [nonebot2](https://github.com/nonebot/nonebot2) 的原神QQ群聊机器人
#### 特别鸣谢  
[MingxuanGame](https://github.com/MingxuanGame) 的人物武器名字自动纠正功能  
[小灰灰](https://github.com/MiniGrayGay) 的人物武器信息api  
### 环境
请务必使用**Python3.7**以上版本！！ 

### 更新记录
2021-4-5 优化涩图速度增加，增加涩图关键词搜索  
2021-4-3 全部移植到nonebot2,增加防撤回，戳一戳等功能  
.  
.  
.  
2021-3-14 第一次更新  
### 部署方法
1 .卸载以前的nonebot  
```shell
pip3 uninstall nonebot
```  
2.安装依赖库
```shell
pip3 install -r requirements.txt
```  
3.在.env和.env.dev文件中设置所需的cookie和SUPERUSERS(超级用户)  
4.在config.hjson文件中设置Bot的QQ账号密码  
```config.hjson
// QQ号
uin: 10001
// QQ密码
password: "abc123"
```
5.运行go-cqhttp  
Windows下运行 go-cqhttp.exe  
Linux下运行 ./go-cqhttplinux  
6.运行Bot.py  
```shell
python3 bot.py
```
7.搭建成功，发送help获取菜单  
<img src="https://github.com/XiaoMiku01/PaimonBot/blob/main/doc/help.png" width="250px" />  
### 目前功能
1.米游社资料查询  
<img src="https://github.com/XiaoMiku01/PaimonBot/blob/main/doc/mys.png" width="250px" />  
2.每日副本查询  
<img src="https://github.com/XiaoMiku01/PaimonBot/blob/main/doc/challenge.png" width="250px" />  
3.角色资料查询  
<img src="https://github.com/XiaoMiku01/PaimonBot/blob/main/doc/character2.png" width="250px" />
<img src="https://github.com/XiaoMiku01/PaimonBot/blob/main/doc/character.png" width="250px" />
  
4.在线运行代码(目前支持py / js / c / c++ / c# / java)  
<img src="https://github.com/XiaoMiku01/PaimonBot/blob/main/doc/code.png" width="250px" />    
5.群聊防撤回，戳一戳回复  
<img src="https://github.com/XiaoMiku01/PaimonBot/blob/main/doc/other.png" width="250px" />  
6.~~涩图~~(不稳定,望谅解！ps超级用户可以回复**撤回**可以撤回最后一条涩图)  
### 注意事项
1.Bot账号请勿使用低等级小号，会导致风控使信息发不出来  
2.若想稳定运行，请在服务器挂一个星期左右   
3.将config.hjson文件中的消息分片打开可降级被风控的概率，不过会导致撤回涩图功能失效
```config.hjson
// 是否强制分片发送消息
// 分片发送将会带来更快的速度
// 但是兼容性会有些问题
force_fragmented: true
```
### 写在最后
本人能力较低，有些代码写的可能比较烂，请大佬亲喷，谢谢！  
发现什么bug或者想要功能欢迎大家提iss和Pr。
