import nonebot as rcnb

__plugin_name = 'other'

other = rcnb.CommandGroup('other', only_to_me=False)


@other.command('chat')
async def _(session: rcnb.CommandSession):
    await session.finish("派蒙现在还听不懂哦，\n@我 help ，获取功能哦！[CQ:image,file=file:///www/wwwroot/PaimonBot/Bot/face/face1.png]")
    return


# @other.command('chat')
# async def _(session: rcnb.CommandSession):
#     await session.finish("派蒙正在适应香港哦，所有功能可能失效几天！！[CQ:image,file=90aa3d3a9635b56bf4c4d00b436f5981.image,url=https://uploadstatic.mihoyo.com/ys-obc/2020/03/12/4820086/701d98b82183919e58afcef508981cbc_2599105281229745644.png?x-oss-process=image/quality,q_70/resize,p_80]")
#     return


@rcnb.on_natural_language()
async def _(session: rcnb.NLPSession):
    return rcnb.IntentCommand(90.0, ('other', 'chat'), {'msg': session.msg_text})
