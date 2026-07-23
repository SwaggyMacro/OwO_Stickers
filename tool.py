# Author: SwaggyMacro
# Created: 2024-08-30
# Description: A script to add new emoji to OwO_Stickers json file

import json
import os

# the emoji name, will be the name of the new emoji in the JSON
# 表情包的名字，将会是新表情包的名字
emoji_name = "红星小狗"

# the emoji data structure
# 表情包的数据结构
emoji_data = f'{{"{emoji_name}": {{ "type": "image", "container": []}}}}'
emoji_data = json.loads(emoji_data)

# the folder where the emoji images are stored
# 表情包图片存放的文件夹
folder = "shapkacto"

# the cdn url of the emoji images, end without slash /
# 表情包JSON的CDN地址，不要以斜杠结尾
cdn_url = "//raw.githubusercontent.com/SwaggyMacro/OwO_Stickers/main/stickers"

# url of the raw json file
# JSON文件的URL
owo_json_url = "OwO.min.json"

# the property where the new emoji data will be appended after, for example below is append after `TG小黄鸭`
# 新表情包数据将会被添加到的位置（比如以下是添加到`TG小黄鸭`的后面）
append_after = "小黄鸭"

# compress the json file
# 是否压缩JSON文件
need_compress = True

# get the json file
# 获取JSON文件
with open("OwO.min.json", "r", encoding="utf-8") as f:
    owo_json = json.load(f)

for index, file  in enumerate(os.listdir("stickers" + os.sep + folder)):
    if file:
        emoji_data[emoji_name]["container"].append(
            {"text": f"{folder}-{index}", "icon":f"<img src='{cdn_url}/{folder}-Preview/{file.replace(".avif", ".webp")}' "
                                                 f"origin='{cdn_url}/{folder}/{file}'>" ,})

# find the index of the append_after, and insert the new emoji data after it
append_index = 0
for i, key in enumerate(owo_json.keys()):
    if key == append_after:
        append_index = i + 1
        break
# insert the new emoji data into the json
owo_json_list = list(owo_json.items())
owo_json_list.insert(append_index, (emoji_name, emoji_data[emoji_name]))
owo_json = dict(owo_json_list)

if need_compress:
    file_content = json.dumps(owo_json, separators=(',', ':'), ensure_ascii=False)
else:
    file_content = json.dumps(owo_json, indent=4, ensure_ascii=False)

with open("OwO.min.json", "w", encoding="utf-8") as f:
    f.write(file_content)

print(file_content)