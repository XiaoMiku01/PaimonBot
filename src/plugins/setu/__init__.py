from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Message, GroupMessageEvent, PrivateMessageEvent,Event
import nonebot
from nonebot.rule import to_me
from httpx import AsyncClient
from .getPic import ghs_pic3
import requests
setu = on_command('setu',aliases={'无内鬼','涩图','色图'})
withdraw = on_command('撤回')
mid = {}
@setu.handle()
async def _(bot:Bot,event:Event):
    global mid
    key =str(event.get_message()).strip()
    pic =await ghs_pic3(key)
    try:
        mid = await setu.send(message=Message(pic),at_sender=True)
    except:
        await setu.send(message=Message('消息被风控，派蒙不背锅'), at_sender=True)

@withdraw.handle()
async def _(bot:Bot,event:Event):
    global mid
    if mid:
        if event.get_user_id() in nonebot.get_driver().config.superusers:
            await bot.delete_msg(message_id=mid['message_id'])
            mid = ''
        else:
            await withdraw.finish('你没有权利撤回哦')
