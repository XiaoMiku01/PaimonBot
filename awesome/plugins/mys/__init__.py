from nonebot import on_command, CommandSession

from .data_source import get_weather_of_city

@on_command('查询')
async def weather(session: CommandSession):
    uid = session.get('uid',prompt='你想查询哪个uid呢？')
    weather_report = await get_weather_of_city(uid)
    await session.send(weather_report)


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['uid'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的uid不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg
