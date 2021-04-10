from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Message, GroupMessageEvent, MessageEvent, Event
import nonebot
from .getPic import ghs_pic3
import json
import re

setu = on_command('setu', aliases={'无内鬼', '涩图', '色图'})
withdraw = on_command('撤回')
cdTime = nonebot.get_driver().config.cdtime


@setu.handle()
async def _(bot: Bot, event: Event):
    global mid
    qid = event.get_user_id()
    data = readJson()
    try:
        cd = event.time - data[qid][0]
    except:
        cd = cdTime + 1
    print(cd)
    key = str(event.get_message()).strip()
    pic = await ghs_pic3(key)
    try:
        if cd > cdTime or event.get_user_id() in nonebot.get_driver().config.superusers:
            await setu.send('给大佬递图', at_sender=True)
            mid = await setu.send(message=Message(pic))
            print(mid)
            writeJson(qid, event.time, mid['message_id'], data)
        else:
            await setu.send(f'不要发的太快，冲多了对身体不好，你的CD还有{cdTime - cd}秒', at_sender=True)
    except Exception as e:
        print(e)
        await setu.send(message=Message('消息被风控，派蒙不背锅'), at_sender=True)


@withdraw.handle()
async def _(bot: Bot, event:GroupMessageEvent):
    tem = str(event.get_message())
    qid = re.findall(r"\d+", tem)[0]
    print(qid)
    if event.get_user_id() in nonebot.get_driver().config.superusers:
        try:
            mid = readJson()[qid][1]
        except Exception as e:
            print(e)
            await  withdraw.finish('只能撤回他最后一次涩图')
            return
        await bot.delete_msg(message_id=mid)
    else:
        await withdraw.finish('你没有权利撤回哦')


def readJson():
    with open(r'./src/plugins/setu/userscd.json', 'r') as f_in:
        data = json.load(f_in)
        f_in.close()
        return data


def writeJson(qid: str, time: int, mid: int, data: dict):
    data[qid] = [time, mid]
    with open(r'./src/plugins/setu/userscd.json', 'w') as f_out:
        json.dump(data, f_out)
        f_out.close()
