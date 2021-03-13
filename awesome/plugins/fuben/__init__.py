from nonebot import on_command, CommandSession
from datetime import datetime

dayOfWeek = datetime.now().isoweekday()


@on_command('周本', aliases=('龙狼', '龙狼公子'))
async def zhouben(session: CommandSession):
    await session.send(
        '[CQ:image,file=0cdf0c673e1b84c7aaba19b72f779091.image,url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-509004439-0CDF0C673E1B84C7AABA19B72F779091/0?term=3]')


@on_command('武器', aliases=('武器本', '武器材料', '武器突破', '今日武器'))
async def wuqi(session: CommandSession):
    if dayOfWeek == 1 or dayOfWeek == 4:
        await session.send(
            '[CQ:image,file=391cde29053030b34666a551d0cfafeb.image,url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-3546299377-391CDE29053030B34666A551D0CFAFEB/0?term=3]')
    elif dayOfWeek == 2 or dayOfWeek == 5:
        await session.send(
            '[CQ:image,file=853a6b22f07a3f38b3bbf1b9aaef945c.image,url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-1793322970-853A6B22F07A3F38B3BBF1B9AAEF945C/0?term=3]')
    elif dayOfWeek == 3 or dayOfWeek == 6:
        await  session.send(
            '[CQ:image,file=ee0c35f2b083f99d170be759d0129a95.image,url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-3359807835-EE0C35F2B083F99D170BE759D0129A95/0?term=3]')
    else:
        await  session.send("今天的副本想打什么打什么哦！")

@on_command('天赋', aliases=('天赋本', '天赋材料', '今日天赋'))
async def tianfu(session: CommandSession):
    if dayOfWeek == 1 or dayOfWeek == 4:
        await session.send(
            '[CQ:image,file=bd57990eb975e79dd56415f5c4a486f8.image,url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-2493272290-BD57990EB975E79DD56415F5C4A486F8/0?term=3]')
    elif dayOfWeek == 2 or dayOfWeek == 5:
        await session.send(
            '[CQ:image,file=67096e669cb47eb5c273a55e28cdc6ab.image,url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-171971510-67096E669CB47EB5C273A55E28CDC6AB/0?term=3]')
    elif dayOfWeek == 3 or dayOfWeek == 6:
        await  session.send(
            '[CQ:image,file=22a8664f136ed902520a7d5002048e6e.image,url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-172246107-22A8664F136ED902520A7D5002048E6E/0?term=3]')
    else:
        await  session.send("今天的副本想打什么打什么哦！[CQ:image,file=2186db2ceefe0c0112df3fb626f66045.image,url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-2060887422-2186DB2CEEFE0C0112DF3FB626F66045/0?term=3]")

if __name__ == '__main__':
    print(dayOfWeek)
