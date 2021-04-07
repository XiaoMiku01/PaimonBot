from nonebot import on_command
from .get_data import get_weapon
from nonebot.adapters.cqhttp import Event, Bot, Message

wea = on_command('武器查询',aliases={'武器资料'})


@wea.handle()
async def _(bot: Bot, event: Event):
    name = str(event.get_message()).strip()
    re =await get_weapon(name)
    await wea.finish(message=Message(re))