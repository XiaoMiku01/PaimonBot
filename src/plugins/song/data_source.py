import httpx


class dataApi():
    '''
    从网易云音乐接口直接获取数据（实验性）
    '''
    headers = {"referer": "http://music.163.com"}
    cookies = {"appver": "2.0.2"}

    async def search(self, songName: str):
        '''
        搜索接口，用于由歌曲名查找id
        '''
        async with httpx.AsyncClient() as client:
            r = await client.post(
                f"http://music.163.com/api/search/get/",
                data={"s": songName, "limit": 5, "type": 1, "offset": 0},
                headers=self.headers,
                cookies=self.cookies
            )
        jsonified_r = r.json()
        if "result" not in jsonified_r:
            raise APINotWorkingException(r.text)
        return jsonified_r

    async def getHotComments(self, songId: int):
        pass
    async def getSongInfo(self, songId: int):
        pass

class dataGet(dataApi):
    '''
    从dataApi获取数据，并做简单处理
    '''

    api = dataApi()

    async def songIds(self, songName: str, amount=5) -> list:
        '''
        根据用户输入的songName 获取候选songId列表 [默认songId数量：5]
        '''
        songIds = list()
        r = await self.api.search(songName=songName)
        idRange = amount if amount < len(
            r["result"]["songs"]) else len(r["result"]["songs"])
        for i in range(idRange):
            songIds.append(r["result"]["songs"][i]["id"])
        return songIds

    async def songComments(self, songId: int, amount=3) -> dict:
        pass

    async def songInfo(self, songId: int) -> dict:
        pass


class dataProcess():
    '''
    将获取的数据处理为用户能看懂的形式
    '''

    @staticmethod
    async def mergeSongInfo(songInfos: list) -> str:
        '''
        将歌曲信息list处理为字符串，供用户点歌
        传递进的歌曲信息list含有多个歌曲信息dict
        '''
        songInfoMessage = "请输入欲点播歌曲的序号：\n"
        numId = 0
        for songInfo in songInfos:
            songInfoMessage += f"{numId}："
            songInfoMessage += songInfo["songName"]
            songInfoMessage += "-"
            songInfoMessage += songInfo["songArtists"]
            songInfoMessage += " 专辑："
            songInfoMessage += songInfo["songAlbum"]
            songInfoMessage += "\n"
            numId += 1
        return songInfoMessage

    @staticmethod
    async def mergeSongComments(songComments: dict) -> str:
        songCommentsMessage = '\n'.join(
            ['%s： %s' % (key, value) for (key, value) in songComments.items()])
        return songCommentsMessage


class APINotWorkingException(Exception):
    def __init__(self, wrongData):
        self.uniExceptionTip="网易云音乐接口返回了意料之外的数据：\n"
        self.wrongData = wrongData

    def __str__(self):
        return self.uniExceptionTip+self.wrongData
