from PIL import Image, ImageDraw, ImageFont, ImageFilter
import time
from io import BytesIO
from base64 import b64encode

from .getData import GetInfo


async def circle_corner(radimg, radii):
    circle = Image.new('L', (radii * 2, radii * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radii * 2, radii * 2), fill=255)

    radimg = radimg.convert("RGBA")
    w, h = radimg.size

    alpha = Image.new('L', radimg.size, 255)
    alpha.paste(circle.crop((0, 0, radii, radii)), (0, 0))
    alpha.paste(circle.crop((radii, 0, radii * 2, radii)), (w - radii, 0))
    alpha.paste(circle.crop((radii, radii, radii * 2, radii * 2)), (w - radii, h - radii))
    alpha.paste(circle.crop((0, radii, radii, radii * 2)), (0, h - radii))

    radimg.putalpha(alpha)
    return radimg


def ys_font(size):
    return ImageFont.truetype(r"./src/data/mys/yuanshen.ttf", size=size, encoding="utf-8")


async def draw_pic(uid):
    raw_data = await GetInfo(uid)
    if (raw_data["retcode"] != 0):
        if (raw_data["retcode"] == 10001):
            return ("Cookie错误/过期，请重置Cookie")
        return (
                "Api报错，返回内容为：\r\n"
                + str(raw_data) + "\r\n出现这种情况可能的UID输入错误 or 不存在"
        )
    else:
        pass
    raw_data = raw_data['data']
    bg_path = r'./src/data/mys/texture2d/bg_1.jpg'
    char1_id = raw_data['avatars'][0]['id']
    char2_id = raw_data['avatars'][1]['id']
    char3_id = raw_data['avatars'][2]['id']
    char4_id = raw_data['avatars'][3]['id']
    char5_id = raw_data['avatars'][4]['id']
    char6_id = raw_data['avatars'][5]['id']

    char1 = f'./src/data/mys/chars/{char1_id}.png'
    char2 = f'./src/data/mys/chars/{char2_id}.png'
    char3 = f'./src/data/mys/chars/{char3_id}.png'
    char4 = f'./src/data/mys/chars/{char4_id}.png'
    char5 = f'./src/data/mys/chars/{char5_id}.png'
    char6 = f'./src/data/mys/chars/{char6_id}.png'
    area = (0, 0, 680, 750)
    img = Image.open(bg_path).crop(area)
    im_blur = img.filter(ImageFilter.GaussianBlur)
    base_img = Image.new("RGB", img.size, (255, 255, 255))
    canvas_img = Image.new("RGB", (int(img.size[0] * 0.95), int(img.size[1] * 0.98)), "black")
    paste_box_x = base_img.size[0] - canvas_img.size[0]
    paste_box_y = base_img.size[1] - canvas_img.size[1]
    paste_box = (int(paste_box_x / 2), int(paste_box_y / 2))
    base_img.paste(canvas_img, paste_box)
    img_canvas = Image.blend(im_blur, base_img, 0.2)

    text_draw = ImageDraw.Draw(img_canvas)

    # ava_holder = Image.open(r'./src/data/mys/texture2d/ba.png').resize((200, 200),
    #                                                       Image.BILINEAR)
    id_img = Image.open(r"./src/data/mys/texture2d/level.png").resize((250, 155),
                                                                      Image.BILINEAR).convert(
        "RGBA")
    # level_img = Image.open(r"./src/data/mys/texture2d/level2.png").resize((180, 180),
    #                                                          Image.BILINEAR).convert(
    #     "RGBA")
    p1_img = Image.open(r"./src/data/mys/texture2d/p1.png").resize((600, 300),
                                                                   Image.BILINEAR).convert(
        "RGBA")
    ava_img = Image.open(r'./src/data/mys/texture2d/UI_EmotionIcon51.png').resize(
        (127, 127), Image.BILINEAR)
    bar = Image.open(r"./src/data/mys/texture2d/bar.png").convert("RGBA").resize((580, 40),
                                                                                 Image.BILINEAR)
    wind_img = Image.open(r"./src/data/mys/texture2d/wind.png").convert("RGBA")
    earth_img = Image.open(r"./src/data/mys/texture2d/earth.png").convert("RGBA")

    char1_img = Image.open(char1).convert("RGBA").resize((95, 95), Image.BILINEAR)
    char2_img = Image.open(char2).convert("RGBA").resize((95, 95), Image.BILINEAR)
    char3_img = Image.open(char3).convert("RGBA").resize((95, 95), Image.BILINEAR)
    char4_img = Image.open(char4).convert("RGBA").resize((95, 95), Image.BILINEAR)
    char5_img = Image.open(char5).convert("RGBA").resize((95, 95), Image.BILINEAR)
    char6_img = Image.open(char6).convert("RGBA").resize((95, 95), Image.BILINEAR)

    # cover_img = Image.open(r"./src/data/mys/texture2d/cover.png").convert("RGBA").resize(
    #     (105, 105), Image.BILINEAR)
    # ava_rad = await circle_corner(ava_img, 15)
    # img_canvas.paste(ava_holder, (15, 20), ava_holder)
    # img_canvas.paste(ava_rad, (50, 55), ava_rad)
    img_canvas.paste(id_img, (210, 45), id_img)
    # img_canvas.paste(level_img, (465, 30), level_img)
    img_canvas.paste(p1_img, (41, 230), p1_img)
    img_canvas.paste(bar, (45, 480), bar)
    img_canvas.paste(wind_img, (308, 240), wind_img)
    img_canvas.paste(earth_img, (480, 245), earth_img)
    img_canvas.paste(char1_img, (40, 540), char1_img)
    img_canvas.paste(char2_img, (140, 540), char2_img)
    img_canvas.paste(char3_img, (240, 540), char3_img)
    img_canvas.paste(char4_img, (340, 540), char4_img)
    img_canvas.paste(char5_img, (440, 540), char5_img)
    img_canvas.paste(char6_img, (540, 540), char6_img)

    # text_draw.text((240, 80), "ABC", 'lightcyan', ys_font(23))
    text_draw.text((230, 80), 'UID ' + f"{uid}", 'lightcyan', ys_font(25))
    if uid[0] == "1":
        text_draw.text((230, 130), '服务器 ' + "天空岛", 'lightcyan', ys_font(25))
    else:
        text_draw.text((220, 130), '服务器 ' + "世界树", 'lightcyan', ys_font(25))
    # text_draw.text((520, 90), "55级", (0, 0, 0), ys_font(30))
    # text_draw.text((510, 125), "世界等级 8", (0, 0, 0), ys_font(18))
    #
    wind_num = raw_data['stats']['anemoculus_number']
    earth_num = raw_data['stats']['geoculus_number']

    char_data = raw_data["avatars"]
    #
    text_draw.text((80, 245), '活跃天数   ' + str(raw_data['stats']['active_day_number']), (0, 0, 0), ys_font(23))
    text_draw.text((80, 285), '成就解锁   ' + str(raw_data['stats']['achievement_number']), (0, 0, 0), ys_font(23))
    text_draw.text((80, 325), '华丽宝箱   ' + str(raw_data['stats']['luxurious_chest_number']), (0, 0, 0), ys_font(23))
    text_draw.text((80, 365), '珍贵宝箱   ' + str(raw_data['stats']['precious_chest_number']), (0, 0, 0), ys_font(23))
    text_draw.text((80, 405), '精致宝箱   ' + str(raw_data['stats']['exquisite_chest_number']), (0, 0, 0), ys_font(23))
    text_draw.text((80, 445), '普通宝箱   ' + str(raw_data['stats']['common_chest_number']), (0, 0, 0), ys_font(23))
    text_draw.text((250, 485), '深境螺旋  ' + raw_data['stats']['spiral_abyss'], 'lightcyan', ys_font(25))
    text_draw.text((320, 365), f'风神瞳\n{wind_num}/66', (0, 0, 0), ys_font(27))
    text_draw.text((490, 365), f'岩神瞳\n{earth_num}/131', (0, 0, 0), ys_font(27))
    text_draw.text((60, 640),
                   f'{char_data[0]["name"]}\nLv.{str(char_data[0]["level"])}\n好感等级{str(char_data[0]["fetter"])}',
                   'lightcyan', ys_font(17))
    text_draw.text((156, 640),
                   f'{char_data[1]["name"]}\nLv.{str(char_data[1]["level"])}\n好感等级{str(char_data[1]["fetter"])}',
                   'lightcyan', ys_font(17))
    text_draw.text((254, 640),
                   f'{char_data[2]["name"]}\nLv.{str(char_data[2]["level"])}\n好感等级{str(char_data[2]["fetter"])}',
                   'lightcyan', ys_font(17))
    text_draw.text((352, 640),
                   f'{char_data[3]["name"]}\nLv.{str(char_data[3]["level"])}\n好感等级{str(char_data[3]["fetter"])}',
                   'lightcyan', ys_font(17))
    text_draw.text((450, 640),
                   f'{char_data[4]["name"]}\nLv.{str(char_data[4]["level"])}\n好感等级{str(char_data[4]["fetter"])}',
                   'lightcyan', ys_font(17))
    text_draw.text((548, 640),
                   f'{char_data[5]["name"]}\nLv.{str(char_data[5]["level"])}\n好感等级{str(char_data[5]["fetter"])}',
                   'lightcyan', ys_font(17))
    text_draw.text((55, 715), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' by 晓轩', 'black', ys_font(18))

    result_buffer = BytesIO()
    img_canvas.save(result_buffer, format='png')
    return 'base64://' + b64encode(result_buffer.getvalue()).decode()


if __name__ == '__main__':
    pass
