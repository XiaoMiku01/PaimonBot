from nonebot import on_endswith
from nonebot.adapters.cqhttp import Bot, Event, Message
from datetime import datetime
import os

tf = on_endswith('天赋')
we = on_endswith('武器')
zb = on_endswith('周本')

PATH = os.path.abspath('.')


@zb.handle()
async def _(bot: Bot, event: Event):
    # await zb.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/zb.png]'))
    await zb.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/zb.png]'))


@tf.handle()
async def _(bot: Bot, event: Event):
    mes = str(event.get_message())
    if '一' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/tf1.png]'))
    elif '二' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/tf2.png]'))
    elif '三' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/tf3.png]'))
    elif '四' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/tf4.png]'))
    elif '五' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/tf5.png]'))
    elif '六' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/tf6.png]'))
    else:
        day = str(datetime.now().isoweekday())
        if '明' in mes:
            if day == '7':
                day = '1'
                await tf.finish(
                    message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/tf{day}.png]'))
            elif day == '6':
                await tf.finish(message='明天星期天所有副本都可以刷哦！')
            else:
                day = str(int(day) + 1)
                await tf.finish(
                    message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/tf{day}.png]'))
        elif day != '7':
            await tf.finish(
                message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/tf{day}.png]'))
        else:
            await tf.finish(message='今天星期天所有副本都可以刷哦！')


@we.handle()
async def _(bot: Bot, event: Event):
    mes = str(event.get_message())
    if '一' in mes:
        await we.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/we1.png]'))
    elif '二' in mes:
        await we.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/we2.png]'))
    elif '三' in mes:
        await we.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/we3.png]'))
    elif '四' in mes:
        await we.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/we4.png]'))
    elif '五' in mes:
        await we.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/we5.png]'))
    elif '六' in mes:
        await we.finish(message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/we6.png]'))
    else:
        day = str(datetime.now().isoweekday())
        if '明' in mes:
            if day == '7':
                day = '1'
                await we.finish(
                    message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/we{day}.png]'))
            elif day == '6':
                await tf.finish(message='明天星期天所有副本都可以刷哦！')
            else:
                day = str(int(day) + 1)
                await we.finish(
                    message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/we{day}.png]'))
        elif day != '7':
            await we.finish(
                message=Message(f'[CQ:image,file=http://pic.xiaoxuan.xyz:88/image/we{day}.png]'))
        else:
            await we.finish(message='今天星期天所有副本都可以刷哦！')
