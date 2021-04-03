from datetime import datetime

from nonebot import on_command, CommandSession


@on_command('周本', aliases=('龙狼', '龙狼公子'))
async def zhouben(session: CommandSession):
    await session.send(
        '[CQ:image,file=file:///www/wwwroot/PaimonBot/Bot/awesome/plugins/challenge/zb.png]')


@on_command('武器', aliases=('武器本', '武器材料', '武器突破', '今日武器'))
async def wuqi(session: CommandSession):
    if datetime.now().isoweekday() == 1 or datetime.now().isoweekday() == 4:
        await session.send(
            '[CQ:image,file=file:///www/wwwroot/PaimonBot/Bot/awesome/plugins/challenge/wq14.png]')
    elif datetime.now().isoweekday() == 2 or datetime.now().isoweekday() == 5:
        await session.send(
            '[CQ:image,file=file:///www/wwwroot/PaimonBot/Bot/awesome/plugins/challenge/wq25.png]')
    elif datetime.now().isoweekday() == 3 or datetime.now().isoweekday() == 6:
        await  session.send(
            '[CQ:image,file=file:///www/wwwroot/PaimonBot/Bot/awesome/plugins/challenge/wq36.png]')
    else:
        await  session.send("今天的副本想打什么打什么哦！[CQ:image,file=file:///www/wwwroot/PaimonBot/Bot/face/face3]")


@on_command('天赋', aliases=('天赋本', '天赋材料', '今日天赋'))
async def tianfu(session: CommandSession):
    if datetime.now().isoweekday() == 1 or datetime.now().isoweekday() == 4:
        await session.send(
            '[CQ:image,file=file:///www/wwwroot/PaimonBot/Bot/awesome/plugins/challenge/tf14.png]]')
    elif datetime.now().isoweekday() == 2 or datetime.now().isoweekday() == 5:
        await session.send(
            '[CQ:image,file=file:///www/wwwroot/PaimonBot/Bot/awesome/plugins/challenge/tf25.png]')
    elif datetime.now().isoweekday() == 3 or datetime.now().isoweekday() == 6:
        await  session.send(
            '[CQ:image,file=file:///www/wwwroot/PaimonBot/Bot/awesome/plugins/challenge/tf36.png]')
    else:
        await  session.send("今天的副本想打什么打什么哦![CQ:image,file=file:///www/wwwroot/PaimonBot/Bot/face/face3]")


if __name__ == '__main__':
    print(datetime.now().isoweekday())
