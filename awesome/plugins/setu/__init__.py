from nonebot import on_command, CommandSession
from .getgsh import ghs_pic
# from nonebot import on_natural_language, NLPSession, IntentCommand
@on_command('涩图', aliases=('setu','色图','无内鬼'))
async def setu(session: CommandSession):
    await session.send('请稍等(本功能不稳定，可能会失败）')
    setu =await ghs_pic()
    await session.send(setu)

