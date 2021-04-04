# from nonebot import on_startswith ,on_command,on_notice,on_message
# from nonebot.rule import to_me,endswith
# from nonebot.adapters.cqhttp import Bot, Event,PokeNotifyEvent,Message,GroupRecallNoticeEvent,FriendRecallNoticeEvent
# from nonebot.typing import T_State
# from nonebot.plugin import on
# test = on_startswith("tet",priority=5)
# test2 = on_command("t2",aliases={"测试2","tt"})
# poke = on_notice()
# recall = on_notice()
# t3  = on_message(rule=endswith('666'))
# t4 =on("收到",priority=1,block=False)
# @test.handle()
# async def test1(bot: Bot, event: Event, state: T_State):
#         print(str(event.get_message()))
#         await bot.send_private_msg(user_id=1561900932,message=event.get_message())
#         # await test.finish(event.get_message(),at_sender=True)
#
# @test2.handle()
# async def t2(bot: Bot, event: Event, state: T_State):
#         print(str(event.get_message()))
#         await bot.send_private_msg(user_id=1561900932, message=event.get_message())
# @poke.handle()
# async def _(bot: Bot, event: PokeNotifyEvent):
#         if event.is_tome() and event.user_id != event.self_id:
#                 await poke.finish(message=Message(f'[CQ:poke,qq={event.user_id}])'))
#
# @recall.handle()
# async def _(bot: Bot, event:FriendRecallNoticeEvent):
#         mid = event.message_id
#         meg =  await bot.get_msg(message_id=mid)
#         # msgid =await recall.send(message=Message(meg['message']))
#         img= await bot.get_image(file='be5b09883f0c354cc005661ab31ba539.image')
#         msgid = await recall.send(message=Message('[CQ:image,file=be5b09883f0c354cc005661ab31ba539.image]'))
#         print(img)
# @t3.handle()
# async def _(bot:Bot,event:Event):
#         # print(event.get_message())
#         await bot.send_private_msg(user_id=1561900932, message='收到')
# @t4.handle()
# async def _(bot:Bot,event:Event):
#         print(event)
#         # await bot.send_private_msg(user_id=1561900932, message='test')
