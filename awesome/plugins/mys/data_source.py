
# https://github.com/Womsxd/YuanShen_User_Info
import sys
import json
import time
import string
import random
import hashlib
import requests

mhyVersion = "2.4.0"


def md5(text):
    md5 = hashlib.md5()
    md5.update(text.encode())
    return (md5.hexdigest())


def DSGet():
    global mhyVersion
    if (mhyVersion == "2.1.0"):
        n = md5(mhyVersion)
    elif (mhyVersion == "2.4.0"):
        n = "pbcfcvnfsm5s2w4x3lsq8caor7v8nlqm"
    else:
        mhyVersion = "2.4.0"
        n = "pbcfcvnfsm5s2w4x3lsq8caor7v8nlqm"
    i = str(int(time.time()))
    r = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
    c = md5("salt=" + n + "&t=" + i + "&r=" + r)
    return (i + "," + r + "," + c)


def GetInfo(Uid, ServerID):
    try:
        req = requests.get(
            url="https://api-takumi.mihoyo.com/game_record/genshin/api/index?server=" + ServerID + "&role_id=" + Uid,
            headers={
                'Accept': 'application/json, text/plain, */*',
                'DS': DSGet(),
                'Origin': 'https://webstatic.mihoyo.com',
                'x-rpc-app_version': mhyVersion,
                'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Unspecified Device) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 miHoYoBBS/2.2.0',
                'x-rpc-client_type': '5',
                'Referer': 'https://webstatic.mihoyo.com/app/community-game-records/index.html?v=6',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,en-US;q=0.8',
                'X-Requested-With': 'com.mihoyo.hyperion',
                'Cookie':'UM_distinctid=174bba7e7813bc-0d93fbb0224054-333376b-144000-174bba7e782b9f; mi18nLang=zh-cn; _ga_E36KSL9TFE=GS1.1.1611330164.2.1.1611330369.0; _gid=GA1.2.953430580.1612083770; CNZZDATA1275023096=569536731-1600871848-https%253A%252F%252Fys.mihoyo.com%252F%7C1612096669; _ga_KJ6J9V9VZQ=GS1.1.1612097208.2.1.1612097227.0; _ga=GA1.2.2019832523.1600876290; login_uid=940759; login_ticket=Nx3d6xwZdmjt5FK6kJSZsytonYJIr89SY4nccNkc; account_id=940759; cookie_token=iFzIMCAU2e1txkG1DMSVdwSv7woDu598l1MJJMgn; ltoken=LdNORo3hbgOttkN7WQ9W4gjsk6BJyEYKHMtMYFyB; ltuid=940759'
            }
        )
        return (req.text)
    except:
        print("访问失败，请重试！")
        # sys.exit (1)
        exit()


def JsonAnalysis(JsonText):
    data = json.loads(JsonText)
    if (data["retcode"] != 0):
        return (
                "Api报错，返回内容为：\r\n"
                + JsonText + "\r\n出现这种情况可能的UID输入错误 or 不存在"
        )
    else:
        pass
    Character_Info = "人物："
    Character_List = []
    Character_List = data["data"]["avatars"]
    for i in Character_List:
        if i["element"] == "None":
            Character_Type = "无属性"
        elif i["element"] == "Anemo":
            Character_Type = "风属性"
        elif (i["element"] == "Pyro"):
            Character_Type = "火属性"
        elif (i["element"] == "Geo"):
            Character_Type = "岩属性"
        elif (i["element"] == "Electro"):
            Character_Type = "雷属性"
        elif (i["element"] == "Cryo"):
            Character_Type = "冰属性"
        elif (i["element"] == "Hydro"):
            Character_Type = "水属性"
        else:
            Character_Type = "草属性"
        if (i["name"] == "旅行者"):
            if (i["image"].find("UI_AvatarIcon_PlayerGirl") != -1):
                TempText = (
                        i["name"] + "[萤——妹妹]" +
                        "（" + str(i["level"]) + "级，"
                        + Character_Type + "）"
                )
            elif (i["image"].find("UI_AvatarIcon_PlayerBoy") != -1):
                TempText = (
                        i["name"] + "[空——哥哥]" +
                        "（" + str(i["level"]) + "级，"
                        + Character_Type + "）"
                )
            else:
                TempText = (
                        i["name"] + "[性别判断失败]" +
                        "（" + str(i["level"]) + "级，"
                        + Character_Type + "）"
                )
        else:
            TempText = (
                    i["name"] +
                    "（" + str(i["level"]) + "级，"
                    + "好感度为" + str(i["fetter"]) + "级，"
                    + str(i["rarity"]) +"）"
            )
        Character_Info = Character_Info + TempText
    Account_Info = (
            "活跃天数：" + str(data["data"]["stats"]["active_day_number"]) +
            "，一共达成了" + str(data["data"]["stats"]["achievement_number"]) +
            "个成就，风神瞳收集了" + str(data["data"]["stats"]["anemoculus_number"]) +
            "个，岩神瞳收集了" + str(data["data"]["stats"]["geoculus_number"]) +
            "个，目前获得了" + str(data["data"]["stats"]["avatar_number"]) +
            "个角色，解锁了" + str(data["data"]["stats"]["way_point_number"]) +
            "个传送点和" + str(data["data"]["stats"]["domain_number"]) +
            "个秘境，深境螺旋当期目前"
    )
    if (data["data"]["stats"]["spiral_abyss"] == "-"):
        Account_Info = Account_Info + "没打"
    else:
        Account_Info = Account_Info + "打到了" + data["data"]["stats"]["spiral_abyss"]
    Account_Info = Account_Info + (
            "，一共开启了" + str(data["data"]["stats"]["common_chest_number"]) +
            "个普通宝箱，" + str(data["data"]["stats"]["exquisite_chest_number"]) +
            "个精致宝箱，" + str(data["data"]["stats"]["precious_chest_number"]) +
            "个珍贵宝箱，" + str(data["data"]["stats"]["luxurious_chest_number"]) +
            "个华丽宝箱"
    )
    Prestige_Info = "声望信息："
    Prestige_list = []
    Prestige_list = data["data"]["city_explorations"]
    for i in Prestige_list:
        Prestige_Info = (Prestige_Info + i["name"] +
                         "的探索进度为" + str(i["exploration_percentage"] / 10) +
                         "%，声望等级为：" + str(i["level"]) + "级")
    return (Account_Info)


async def get_weather_of_city(uid: str) -> str:
    try:
        uid = str(int(uid))
    except:
        return "输入有误！"
    if (len(uid) == 9):
        if (uid[0] == "1"):
            UidInfo = JsonAnalysis(GetInfo(uid, "cn_gf01"))
            return  "查询成功：\r\n" + UidInfo
        elif (uid[0] == "5"):
            UidInfo = JsonAnalysis(GetInfo(uid, "cn_qd01"))
            return "查询成功：\r\n" + UidInfo
        else:
            return "UID输入有误！！\r\n请检查UID是否为国服UID！"
    else:
        return "UID长度有误！！\r\n请检查输入的UID是否为9位数！"

# async def get_weather_of_city(city: str) -> str:
#     return f'{city}的天气是……'