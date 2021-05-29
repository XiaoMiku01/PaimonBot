from nonebot import on_notice, on_message,on_command
from nonebot.adapters.cqhttp import GroupRecallNoticeEvent, Bot, Message, FriendRecallNoticeEvent, PokeNotifyEvent, \
    MessageEvent,PrivateMessageEvent,GroupMessageEvent
from nonebot.rule import to_me
import random
last_message = ''
poke = on_notice(rule=to_me(),block=False)
recall = on_notice(block=False)
flashimg = on_message(block=False)
blockrepeat = on_message(block=False)

# 群聊
@recall.handle()
async def _(bot: Bot, event: GroupRecallNoticeEvent):
    mid = event.message_id
    meg = await bot.get_msg(message_id=mid)
    if event.user_id != event.self_id and 'type=flash,' not in meg['message']:
        re = '刚刚说了:' + meg['message'] + '\n不要以为派蒙没看见！'
        await recall.finish(message=Message(re), at_sender=True)


# 私聊
@recall.handle()
async def _(bot: Bot, event: FriendRecallNoticeEvent):

     mid = event.message_id
     meg = await bot.get_msg(message_id=mid)
     if event.user_id != event.self_id and 'type=flash,' not in meg['message']:
        re = '刚刚说了:' + str(meg['message']) + '\n不要以为派蒙没看见！'
        await recall.finish(message=Message(re))


@poke.handle()
async def _poke(bot: Bot, event: PokeNotifyEvent, state: dict) -> None:
    msg =random.choice([
        "你再戳！", "？再戳试试？", "别戳了别戳了再戳就坏了555", "我爪巴爪巴，球球别再戳了", "你戳你🐎呢？！",
        "那...那里...那里不能戳...绝对...", "(。´・ω・)ん?", "有事恁叫我，别天天一个劲戳戳戳！", "欸很烦欸！你戳🔨呢",
        "?", "差不多得了😅", "欺负咱这好吗？这不好", "我希望你耗子尾汁"
    ])

    await poke.finish(msg, at_sender=True)


@flashimg.handle()
async def _(bot: Bot, event: MessageEvent):
    msg = str(event.get_message())
    if 'type=flash,' in msg:
        msg = msg.replace('type=flash,', '')
        await flashimg.finish(message=Message("不要发闪照，好东西就要分享。" + msg), at_sender=True)

@blockrepeat.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    global last_message
    message = (event.get_message())
    if message == last_message:
        tem = "打断复读" + random.randint(1, 10) * '!'
        last_message = tem
        await blockrepeat.finish(message=tem)
    else:
        last_message = message
