from nonebot import on_command, CommandSession


@on_command('help', aliases=('帮助'))
async def help(session: CommandSession):
    await session.finish('1.发送 [查询<空格><uid>] 查询米游社资料\neg. 查询 100000001\n2.发送 [武器/今日武器] 查看今日武器材料和武器\n3.发送 [天赋/今日天赋] '
                         '查看今日天赋材料和人物\n '
                         + '4.发送 [周本] 查看周本材料和人物\n'
                         + '5.发送 [武器查询<空格>武器名] 查看武器资料\n' + 'eg. 武器资料 狼末' + '\n'
                         + '6.发送 [角色资料<空格>名字 ] 查看人物简介\neg. 角色资料 琴\n'
                         + '7.发送 [命座<空格>名字 ] 查看人物命座\neg. 命座 [琴/琴四命]\n '
                         + '8.发送[涩图/setu]（不稳定）\n'
                         + '发送前记得要@派蒙哦！')
