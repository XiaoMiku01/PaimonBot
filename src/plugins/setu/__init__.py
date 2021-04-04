from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Message, GroupMessageEvent, PrivateMessageEvent, Event
import nonebot
from httpx import AsyncClient

setu = on_command('setu', aliases={'无内鬼', '涩图', '色图'})
withdraw = on_command('撤回')
mid = {}


@setu.handle()
async def _(bot: Bot, event: Event):
    global mid
    pic = await ghs_pic()
    mid = await setu.send(message=Message(pic), at_sender=True)


@withdraw.handle()
async def _(bot: Bot, event: Event):
    global mid
    if mid:
        if event.get_user_id() in nonebot.get_driver().config.superusers:
            await bot.delete_msg(message_id=mid['message_id'])
            mid = ''
        else:
            await withdraw.finish('你没有权利撤回哦')


apikey = nonebot.get_driver().config.apikey


async def ghs_pic() -> str:
    async with AsyncClient() as client:
        try:
            req_url = "https://api.lolicon.app/setu/"
            params = {"apikey": apikey,
                      "r18": 0,
                      "size1200": True}
            res = await client.get(req_url, params=params)
            setu_title = res.json()['data'][0]['title']
            setu_url = res.json()['data'][0]['url']
            setu_pid = res.json()['data'][0]['pid']
            setu_author = res.json()['data'][0]['author']
            local_img_url = "title:" + setu_title + "[CQ:image,file=" + setu_url + "]" + "pid:" + str(
                setu_pid) + " 画师:" + setu_author
            return local_img_url
        except Exception as e:
            print(e)
            return "阿这，出了一点问题"
