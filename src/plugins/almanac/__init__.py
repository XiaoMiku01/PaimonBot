from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Message, GroupMessageEvent, PrivateMessageEvent

from .getPic import get_almanac_base64_str

almanac = on_command('黄历', aliases={'原神黄历'})


@almanac.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    ba = get_almanac_base64_str()
    await almanac.send(Message(f'[CQ:image,file={ba}]'))


@almanac.handle()
async def _(bot: Bot, event: PrivateMessageEvent):
    ba = get_almanac_base64_str()
    await almanac.send(Message(f'[CQ:image,file={ba}]'))
