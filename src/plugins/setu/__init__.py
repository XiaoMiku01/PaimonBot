from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Message, GroupMessageEvent, PrivateMessageEvent, Event
import nonebot
from .getPic import ghs_pic3
import json

setu = on_command('setu', aliases={'无内鬼', '涩图', '色图'})
withdraw = on_command('撤回')
mid = {}
cdTime=nonebot.get_driver().config.cdtime

@setu.handle()
async def _(bot: Bot, event: Event):
    global mid
    cd = timeDiff(event.get_user_id(), event.time)
    key = str(event.get_message()).strip()
    pic = await ghs_pic3(key)
    try:
        if cd>60 or event.get_user_id() in nonebot.get_driver().config.superusers:
            await setu.send('给大佬递图', at_sender=True)
            mid = await setu.send(message=Message(pic))
        else:
            await setu.send(f'不要发的太快，冲多了对身体不好，你的CD还有{60-cdTime}秒', at_sender=True)
    except:
        await setu.send(message=Message('消息被风控，或者api调用达到上限，派蒙不背锅'), at_sender=True)


@withdraw.handle()
async def _(bot: Bot, event: Event):
    global mid
    if mid:
        if event.get_user_id() in nonebot.get_driver().config.superusers:
            await bot.delete_msg(message_id=mid['message_id'])
            mid = ''
        else:
            await withdraw.finish('你没有权利撤回哦')


def timeDiff(id: str, time: int):
    with open(r'./src/plugins/setu/userscd.json', 'r') as f_in:
        data = json.load(f_in)
        try:
            time_old = data[id]
        except:
            time_old = 0
        data[id] = time
        with open(r'./src/plugins/setu/userscd.json', 'w') as f_out:
            json.dump(data, f_out)
            f_in.close()
            f_out.close()
            return time - time_old
