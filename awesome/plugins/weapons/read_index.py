# 补全文件专用
# 如果不了解这个，请不要运行
# MingxuanGame 最后于2021/4/3
import json

from xpinyin import Pinyin


def run():
    with open("data.json", "r", encoding="utf-8") as f:
        source = json.loads(f.read())

    weapon_list = []
    for d in source:
        name = d["name"][0]
        weapon_dict = {d["name"][0]: Pinyin().get_pinyin(name).split("-")}
        weapon_list.append(weapon_dict)

    with open("weapon_index.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(weapon_list, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    run()
