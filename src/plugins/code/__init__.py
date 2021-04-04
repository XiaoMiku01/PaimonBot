from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
from .run import run

runcode = on_command('super')


@runcode.handle()
async def _(bot: Bot, event: Event):
    code = str(event.get_message()).strip()
    res = await run(code)
    await runcode.send(message='\n' + res, at_sender=True)
