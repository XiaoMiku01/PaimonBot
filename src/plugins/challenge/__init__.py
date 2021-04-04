from nonebot import on_endswith
from nonebot.adapters.cqhttp import Bot, Event, Message
from datetime import datetime

tf = on_endswith('天赋')
we = on_endswith('武器')
zb = on_endswith('周本')


@zb.handle()
async def _(bot: Bot, event: Event):
    await zb.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/zb.png]'))


@tf.handle()
async def _(bot: Bot, event: Event):
    mes = str(event.get_message())
    if '一' in mes:
        await tf.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/tf1.png]'))
    elif '二' in mes:
        await tf.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/tf2.png]'))
    elif '三' in mes:
        await tf.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/tf3.png]'))
    elif '四' in mes:
        await tf.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/tf4.png]'))
    elif '五' in mes:
        await tf.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/tf5.png]'))
    elif '六' in mes:
        await tf.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/tf6.png]'))
    else:
        day = str(datetime.now().isoweekday())
        if '明' in mes:
            if day == '7':
                day = '1'
                await tf.finish(
                    message=Message(f'[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/tf{day}.png]'))
            else:
                day = str(int(day) + 1)
                await tf.finish(
                    message=Message(f'[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/tf{day}.png]'))
        elif day != '7':
            await tf.finish(
                message=Message(f'[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/tf{day}.png]'))
        else:
            await tf.finish(message='今天星期天所有副本都可以刷哦！')


@we.handle()
async def _(bot: Bot, event: Event):
    mes = str(event.get_message())
    if '一' in mes:
        await we.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/we1.png]'))
    elif '二' in mes:
        await we.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/we2.png]'))
    elif '三' in mes:
        await we.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/we3.png]'))
    elif '四' in mes:
        await we.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/we4.png]'))
    elif '五' in mes:
        await we.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/we5.png]'))
    elif '六' in mes:
        await we.finish(message=Message('[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/we6.png]'))
    else:
        day = str(datetime.now().isoweekday())
        if '明' in mes:
            if day == '7':
                day = '1'
                await we.finish(
                    message=Message(f'[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/we{day}.png]'))
            else:
                day = str(int(day) + 1)
                await we.finish(
                    message=Message(f'[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/we{day}.png]'))
        elif day != '7':
            await we.finish(
                message=Message(f'[CQ:image,file=file:///www/wwwroot/Paimon2/src/data/challenge/we{day}.png]'))
        else:
            await we.finish(message='今天星期天所有副本都可以刷哦！')
