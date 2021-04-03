from nonebot import on_command, CommandSession

from .run import run


@on_command('super', only_to_me=False)
async def run_code(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    session.state['code'] = stripped_arg
    session.state[session.current_key] = stripped_arg
    code = session.get('code')
    res = await run(code)
    await session.send(message='\n' + res, at_sender=True)
