from nonebot import on_command, CommandSession
from .get_data import get_wuqi

@on_command('武器查询',only_to_me=False,aliases=('武器资料','查武器'))
async def wuqi_ziliao(session: CommandSession):
    name = session.get('name',prompt='你想查询哪个武器呢？')
    print(name)
    req = get_wuqi(name)
    await session.send(req)

# @on_command('武器资料', aliases=(names))
# async def wuqi_ziliao(session: CommandSession):
#     name = session.state.get('message') or session.current_arg
#     req = await get_wuqi(name)
#     if req !='没有找到该武器，看看名字写错了没':
#         await session.send(req)

@wuqi_ziliao.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['name'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的武器不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg