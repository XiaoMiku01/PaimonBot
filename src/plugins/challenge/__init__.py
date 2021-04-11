from nonebot import on_regex
from nonebot.adapters.cqhttp import Bot, Event, Message
from datetime import datetime
import os
import re

PATH = os.path.abspath('.')
#获取配置的命令起始字符，以免Bot随便响应
with open(PATH + '/.env.dev', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        if re.match('COMMAND_START', i, flags=0):
            i = re.search('\[.*\]', i, flags=0).group()
            cmd = re.sub('\"', "", i, count=0, flags=0)
            if cmd == r'[]':
                cmd = ""
            break

#通过正则匹配命令起始字符和查询命令
tf = on_regex('^' + cmd + '.*天赋', flags=0)
we = on_regex('^' + cmd + '.*武器', flags=0)
zb = on_regex('^' + cmd + '.*周本', flags=0)

@zb.handle()
async def _(bot: Bot, event: Event):
    await zb.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/zb.png]'))

#修改判断逻辑，减少错误回复产生
@tf.handle()
async def _(bot: Bot, event: Event):
    mes = str(event.get_message())
    day = str(datetime.now().isoweekday())
    if '一' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf1.png]'))
    elif '二' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf2.png]'))
    elif '三' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf3.png]'))
    elif '四' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf4.png]'))
    elif '五' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf5.png]'))
    elif '六' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf6.png]'))
    elif '明' in mes:
        if day == '7':
            day = '1'
            await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf{day}.png]'))
        elif day == '6':
            await tf.finish(message='明天是周日，所有副本都可以刷哦！')
        else:
            day = str(int(day) + 1)
            await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf{day}.png]'))
    elif '日' in mes:
        await tf.finish(message='周日所有副本都可以刷哦！')
    else:
        if day == '7':
            await tf.finish(message='今天是周日，所有副本都可以刷哦！')
        else:
            await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf{day}.png]'))

@we.handle()
async def _(bot: Bot, event: Event):
    mes = str(event.get_message())
    day = str(datetime.now().isoweekday())
    if '一' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we1.png]'))
    elif '二' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we2.png]'))
    elif '三' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we3.png]'))
    elif '四' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we4.png]'))
    elif '五' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we5.png]'))
    elif '六' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we6.png]'))
    elif '明' in mes:
        if day == '7':
            day = '1'
            await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we{day}.png]'))
        elif day == '6':
            await we.finish(message='明天是周日，所有副本都可以刷哦！')
        else:
            day = str(int(day) + 1)
            await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we{day}.png]'))
    elif '日' in mes:
        await we.finish(message='周日所有副本都可以刷哦！')
    else:
        if day == '7':
            await we.finish(message='今天是周日，所有副本都可以刷哦！')
        else:
            await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we{day}.png]'))
