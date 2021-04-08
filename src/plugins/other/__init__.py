from nonebot import on_notice
from nonebot.adapters.cqhttp import GroupRecallNoticeEvent, Bot, Message, FriendRecallNoticeEvent, PokeNotifyEvent
from nonebot.rule import to_me
from random import choice

poke = on_notice(rule=to_me())
recall = on_notice()

# 群聊
@recall.handle()
async def _(bot: Bot, event: GroupRecallNoticeEvent):
    if event.user_id != event.self_id:
        mid = event.message_id
        meg = await bot.get_msg(message_id=mid)
        re = '刚刚说了:' + meg['message'] + '\n不要以为派蒙没看见！'
        await recall.finish(message=Message(re), at_sender=True)
# 私聊
@recall.handle()
async def _(bot: Bot, event: FriendRecallNoticeEvent):
    if event.user_id != event.self_id:
        mid = event.message_id
        meg = await bot.get_msg(message_id=mid)
        re = '刚刚说了:' + meg['message'] + '\n不要以为派蒙没看见！'
        await recall.finish(message=Message(re))

@poke.handle()
async def _poke(bot: Bot, event: PokeNotifyEvent, state: dict) -> None:
    msg = choice([
        "你再戳！", "？再戳试试？", "别戳了别戳了再戳就坏了555", "我爪巴爪巴，球球别再戳了", "你戳你🐎呢？！",
        "那...那里...那里不能戳...绝对...", "(。´・ω・)ん?", "有事恁叫我，别天天一个劲戳戳戳！", "欸很烦欸！你戳🔨呢",
        "?", "差不多得了😅", "欺负咱这好吗？这不好", "我希望你耗子尾汁"
    ])

    await poke.finish(msg, at_sender=True)
