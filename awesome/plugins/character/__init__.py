from nonebot import on_command, CommandSession

from .get_character import get_character, get_mz


@on_command('命座'
            '', only_to_me=False)
async def mz(session: CommandSession):
    name = session.get('name', prompt='你想查询哪个角色呢？')
    req = await get_mz(name)
    await session.send(req)


@mz.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text
    if session.is_first_run:
        if stripped_arg:
            session.state['name'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的角色不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg


@on_command('人物资料', only_to_me=False, aliases=('角色资料', '角色查询', '人物查询', '人物简介', '角色简介'))
async def get_ch(session: CommandSession):
    name = session.get('name', prompt='你想查询哪个角色呢？')
    req = get_character(name)
    await session.send(req)


@get_ch.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['name'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的角色不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg
