import difflib
import json
import os

import requests
from bs4 import BeautifulSoup
from xpinyin import Pinyin

# import ./src.plugins.weapons.read_index

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/89.0.4389.82 Safari/537.36"}


def get_url(name: str):
    re = requests.get(url=f'https://genshin.minigg.cn/?data={name}', headers=headers)
    soup = BeautifulSoup(re.text, "lxml").body
    user_dict = json.loads(soup.text)
    return user_dict['icon']


with open(r"./src/data/weapon/data.json", 'r', encoding='utf-8') as f:
    weapon_all = json.load(f)
weapon_type = {1: "单手剑", 2: "双手剑", 3: "弓", 4: "法器", 5: "长枪"}


async def get_weapon(name: str) -> str:
    name = str(name)
    for i in weapon_all:
        if name in i['name']:
            try:
                url = get_url(i['name'][0])
                weapon_name = url.split('/')[-1]
                icon = f'[CQ:image,file={weapon_name},url={url}]'
            except:
                icon = ''
            return i['name'][0] + '\n' + icon + '\n' + str(i['star']) + '★' * i['star'] + weapon_type[
                i['type']] + '\n' + '1级基础攻击力:' + str(
                i['basic_attack']) + '\n' + '满级基础攻击力:' + str(i['max_attack']) + '\n' + '满级副属性:' + i[
                       'max_attribute'] + '\n' + '技能:' + i['skill']
    correct_result = auto_correct(name)
    if len(correct_result) > 1:
        return f"派蒙这里没找到武器{name}，你是要搜索如下的武器吗?\n{montage_result(correct_result)}"
    elif len(correct_result) < 1:
        return "没有找到该武器,派蒙也米有办法！是不是名字错了？[CQ:image,file=de039db103c31286664f761ff0252cc3.image," \
               "url=http://c2cpicdw.qpic.cn/offpic_new/1561900932//1561900932-292137392" \
               "-DE039DB103C31286664F761FF0252CC3" \
               "/0?term=3] "
    else:
        return f"派蒙这里没找到武器{name}，你是要搜索{correct_result[0]}吗"


def auto_correct(name: str) -> list:
    if not os.path.exists("./weapon_index.json"):
        run()
    with open(r"./src/data/weapon/weapon_index.json", "r", encoding="utf-8") as weapon_index_file:
        character_index = json.loads(weapon_index_file.read())
    input_pin_yin_list = Pinyin().get_pinyin(name).split("-")
    result_cache = []
    result = []
    for index_name in character_index:
        true_name = list(index_name.keys())[0]
        for input_pin_yin in input_pin_yin_list:
            for true_pin_yin in index_name[true_name]:
                if difflib.SequenceMatcher(None, true_pin_yin, input_pin_yin).quick_ratio() >= 1:
                    result_cache.append(true_name)
        if difflib.SequenceMatcher(None, true_name, name).quick_ratio() >= 0.8:
            result_cache.append(true_name)
    for result_repeat in result_cache:
        if result_cache.count(result_repeat) > 1 and result_repeat not in result:
            result.append(result_repeat)
    return result


def montage_result(correct_result: list) -> str:
    cause = correct_result[0]
    for i in range(1, len(correct_result)):
        cause = cause + "\n" + correct_result[i]
    return cause


def run():
    with open(r"./src/data/weapon/data.json", "r", encoding="utf-8") as f:
        source = json.loads(f.read())

    weapon_list = []
    for d in source:
        name = d["name"][0]
        weapon_dict = {d["name"][0]: Pinyin().get_pinyin(name).split("-")}
        weapon_list.append(weapon_dict)

    with open(r"./src/data/weapon/weapon_index.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(weapon_list, ensure_ascii=False, indent=2))
