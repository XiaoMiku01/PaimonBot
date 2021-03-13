import json
import requests
from bs4 import BeautifulSoup
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

def get_url(name: str):
    re = requests.get(url=f'https://genshin.minigg.cn/?data={name}',headers=headers)
    soup = BeautifulSoup(re.text, "lxml").body
    user_dict = json.loads(soup.text)
    return user_dict['icon']


with open(r'C:\Users\15619\Desktop\PaimonBot\Bot\awesome\plugins\wuqi\data.json', 'r', encoding='utf-8') as f:
    all = json.load(f)
wuqitype = {1: "单手剑", 2: "双手剑", 3: "弓", 4: "法器", 5: "长枪"}


def get_wuqi(name: str) -> str:
    name = str(name)
    for i in all:
        if name in i['name']:
            try:
                url = get_url(i['name'][0])
                wuqi_name=url.split('/')[-1]
                icon = f'[CQ:image,file={wuqi_name},url={url}]'
            except:
                icon = ''
            return i['name'][0] + '\n' + icon + '\n' + str(i['star']) + '★' * i['star'] + wuqitype[
                i['type']] + '\n' + '1级基础攻击力:' + str(
                i['basic_attack']) + '\n' + '满级基础攻击力:' + str(i['max_attack']) + '\n' + '满级副属性:' + i[
                       'max_attribute'] + '\n' + '技能:' + i['skill']
    return "没有找到该武器,派蒙也米有办法！是不是名字错了？[CQ:image,file=de039db103c31286664f761ff0252cc3.image,url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-292137392-DE039DB103C31286664F761FF0252CC3/0?term=3]"


if __name__ == '__main__':
    print(get_url('天空之翼'))
