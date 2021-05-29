import base64
from re import findall

import nonebot
from httpx import AsyncClient

apikey = nonebot.get_driver().config.apikey
if nonebot.get_driver().config.setuproxy == 'True':
    proxy = 'i.pixiv.cat'
else:
    proxy = 'disable'


async def ghs_pic3(keyword='') -> str:
    async with AsyncClient() as client:
        req_url = "https://api.lolicon.app/setu/"
        params = {"apikey": apikey,
                  "r18": 0,
                  "size1200": 'true',
                  'keyword': keyword,
                  'proxy': proxy
                  }
        res = await client.get(req_url, params=params)
        try:
            setu_title = res.json()['data'][0]['title']
            setu_url = res.json()['data'][0]['url']
            base64 = await downPic(setu_url)
            setu_pid = res.json()['data'][0]['pid']
            setu_author = res.json()['data'][0]['author']
            pic = "[CQ:image,file=base64://" + base64 + "]"
            local_img_url = "title:" + setu_title + "[CQ:image,file=base64://" + base64 + "]" + "pid:" + str(
                setu_pid) + " 画师:" + setu_author
            # return setu_url
            # return local_img_url
            return pic
        except Exception as e:
            print(res.text)
            print(e)
            if '额度限制' not in res.text:
                return f"图库中没有搜到关于{keyword}的图。今日额度还剩下{res.json()['quota']}次。"
            else:
                return 'api调用已到达上限'


async def downPic(url) -> str:
    async with AsyncClient() as client:
        headers = {
            'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
        re = await client.get(url=url, headers=headers)
        if re:
            ba = str(base64.b64encode(re.content))
            pic = findall(r"\'([^\"]*)\'", ba)[0].replace("'", "")
            return pic


if __name__ == '__main__':
    downPic(ghs_pic3())
