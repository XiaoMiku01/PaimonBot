from .data_source import dataGet, dataProcess
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
from nonebot import on_command


dataget = dataGet()

songpicker = on_command("点歌")


@songpicker.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["songName"] = args


@songpicker.got("songName", prompt="歌名是？")
async def handle_songName(bot: Bot, event: Event, state: T_State):
    songName = state["songName"]
    songIdList = await dataget.songIds(songName=songName)
    if songIdList is None:
        await songpicker.reject("没有找到这首歌，请发送其它歌名！")
    state["songIdList"] = songIdList
    selectedSongId = songIdList[int(0)]
    songContent = [
        {
            "type": "music",
            "data": {
                "type": 163,
                "id": selectedSongId
            }
        }
    ]
    await songpicker.send(songContent)



