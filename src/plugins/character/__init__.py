from nonebot import on_command
from .get_character import get_character, get_mz
from nonebot.adapters.cqhttp import Event, Bot, Message

chara = on_command('人物查询', aliases={'角色资料', '人物查询', '人物简介', '角色简介', '角色查询'})
mz = on_command('命座')


@chara.handle()
async def _(bot: Bot, event: Event):
    name = str(event.get_message()).strip()
    re = get_character(name)
    await chara.finish(message=Message(re))


@mz.handle()
async def _(bot: Bot, event: Event):
    name = str(event.get_message()).strip()
    re = await get_mz(name)
    await chara.finish(message=Message(re))
