from nonebot import on_command, CommandSession

from .getImg import draw_pic

@on_command('查询',only_to_me=False,aliases=('派蒙查询'))
async def weather(session: CommandSession):

    stripped_arg = session.current_arg_text.strip()
    session.state['uid'] = stripped_arg
    session.state[session.current_key] = stripped_arg
    uid = session.get('uid')
    im = await draw_pic(uid)
    await session.send(f'[CQ:image,file={im}]')
