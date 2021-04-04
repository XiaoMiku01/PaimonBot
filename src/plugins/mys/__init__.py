from nonebot import on_command
from nonebot.adapters.cqhttp import Event, Bot, Message

from .getImg import draw_pic

import re

query = on_command('查询')


@query.handle()
async def _(bot: Bot, event: Event):
    message = str(event.get_message())
    try:
        uid = re.findall(r"\d+", message)[0]  # str
        im = await draw_pic(uid)
        await query.send(Message(f'[CQ:image,file={im}]'))
    except:
        await query.send(Message('输入错误！'))
