import nonebot as rcnb

__plugin_name = 'other'

other = rcnb.CommandGroup('other', only_to_me=False)


@other.command('chat')
async def _(session: rcnb.CommandSession):
    await session.finish("派蒙现在还听不懂哦，\n@我 help ，获取功能哦！[CQ:image,file=90aa3d3a9635b56bf4c4d00b436f5981.image,url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-3987012577-90AA3D3A9635B56BF4C4D00B436F5981/0?term=3]")
    return


@rcnb.on_natural_language()
async def _(session: rcnb.NLPSession):
    return rcnb.IntentCommand(90.0, ('other', 'chat'), {'msg': session.msg_text})
