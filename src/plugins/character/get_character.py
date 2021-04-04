import difflib
import json
import re

import bs4
import requests
from xpinyin import Pinyin


def nic2name(name):
    with open(r"./src/data/character/nickname.json", 'r', encoding='utf-8') as f:
        all = json.load(f)
        f.close()
    for i in all:
        for x in i.values():
            if name in x:
                return x[0]
    return name


def get_json(name: str) -> dict:
    name = nic2name(name)
    res = requests.get(f'https://genshin.minigg.cn/?data={name}')
    soup = bs4.BeautifulSoup(res.text, "lxml").body
    character_json = json.loads(soup.text)
    return character_json


def num_to_char(num):
    """数字转中文"""
    num = str(num)
    num_dict = {"0": u"零", "1": u"一", "2": u"二", "3": u"三", "4": u"四", "5": u"五", "6": u"六", "7": u"七", "8": u"八",
                "9": u"九"}
    listnum = list(num)
    shu = []
    for i in listnum:
        shu.append(num_dict[i])
    new_str = "".join(shu)
    return new_str


def char_to_char(char):
    char_dict = {"零": u"0", "一": u"1", "二": u"2", "三": u"3", "四": u"4", "五": u"5", "六": u"6", "七": u"7", "八": u"8",
                 "九": u"9"}
    listnum = list(char)
    shu = []
    for i in listnum:
        shu.append(char_dict[i])
    new_str = "".join(shu)
    return int(new_str)


def get_icon(data: dict) -> str:
    url = data['avatar'].split('?')[0]
    png_name = url.split('/')[-1]
    return f'[CQ:image,file={png_name},url={url}]'


def get_character(name: str) -> str:
    nick_name = nic2name(name)
    try:
        data0 = get_json(nick_name)
        data = data0['角色信息']
        if nick_name == '旅行者':
            data["简介"] = '无'
    except:
        correct_result = auto_correct(nick_name)
        if correct_result is None:
            return f"派蒙这里没找到{name}，可能是派蒙的错，可能是你输入的名字不正确哦。"
        else:
            if len(correct_result) > 1:
                return f"派蒙这里没找到{name}，你是要搜索如下的角色吗?\n{montage_result(correct_result)}"
            elif len(correct_result) < 1:
                return f"派蒙这里没找到{name}，可能是派蒙的错，可能是你输入的名字不正确哦。"
            else:
                return f"派蒙这里没找到{name}，你是要搜索{correct_result[0]}吗"
    try:
        result = nick_name + '\n' + get_icon(data0) + '\n' + '命之座：' + str(data['命之座']) + '\n' + '所属：' + str(
            data['所属']) + '\n' + '武器类型：' + \
                 str(data['武器类型']) + '\n' + '生日：' + str(data['生日']) + '\n' + '神之眼：' + str(data['神之眼']) + '\n' + '称号：' + \
                 str(data['称号']) + '\n' + '简介：' + str(data['简介'])
    except:
        result = nick_name + '\n' + get_icon(data0) + '\n' + '命之座：' + str(data['命之座']) + '\n' + '所属：' + str(
            data['所属']) + '\n' + '武器类型：' + \
                 str(data['武器类型']) + '\n' + '生日：' + str(data['生日']) + '\n' + '神之心：' + str(data['神之心']) + '\n' + '称号：' + \
                 str(data['称号']) + '\n' + '简介：' + str(data['简介'])
    return result


async def get_mz(name_mz: str) -> str:
    name_mz = name_mz.replace(" ", "")
    try:
        name = re.findall(r'(.*)([零一二三四五六七八九0123456789]{1})命', name_mz)[0][0]
        name = nic2name(name)
    except:
        name = name_mz
        name = nic2name(name)
    try:
        num = int(re.search('\d{1,5}', name_mz).group(0))
    except:
        try:
            num = char_to_char(re.findall(r'(.*)([零一二三四五六七八九0123456789]{1})命', name_mz)[0][1])
        except:
            num = -1
    try:
        data0 = get_json(name)
        data = data0['命之座']
    except:
        return f"派蒙这没有{name}，可能是官方资料没有该资料，可能是你输入的名字不正确哦。"
    result = ''
    if num == -1:
        n = 1
        for key, value in data.items():
            result = result + num_to_char(n) + '命' + key + ':' + str(value['introduction']) + '\n'
            n = n + 1
        return f'{name}' + '\n' + result
    elif 0 < num < 7:
        n = 1
        for key, value in data.items():
            result = num_to_char(num) + '命' + key + ':' + str(value['introduction'])
            if n == num:
                return f'{name}的' + result
            n = n + 1
    elif num == 0:
        return "你搁这原地tp呢？"
    else:
        return f"查询错误!你家{name}有{num}命？？"


def auto_correct(name: str) -> list:
    with open(r"./src/data/character/character_index.json", "r", encoding="utf-8") as f:
        character_index = json.loads(f.read())
    input_pin_yin_list = Pinyin().get_pinyin(name).split("-")
    result_cache = []
    result = []
    for index_name in character_index:
        true_name = list(index_name.keys())[0]
        for input_pin_yin in input_pin_yin_list:
            for true_pin_yin in index_name[true_name]:
                if difflib.SequenceMatcher(None, true_pin_yin, input_pin_yin).quick_ratio() >= 1:
                    result_cache.append(true_name)
        if difflib.SequenceMatcher(None, true_name, name).quick_ratio() >= 0.3:
            result_cache.append(true_name)
    for result_repeat in result_cache:
        if result_cache.count(result_repeat) > 1 and not result_repeat in result:
            result.append(result_repeat)
    return result


def montage_result(correct_result: list) -> str:
    cause = correct_result[0]
    for i in range(1, len(correct_result)):
        cause = cause + "\n" + correct_result[i]
    return cause


if __name__ == '__main__':
    print(get_character('可aaa'))
