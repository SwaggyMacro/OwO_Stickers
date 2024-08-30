# Author: SwaggyMacro
# Created: 2024-08-30
# Description: A script to add new emoji to OwO_Stickers json file

import json
import os
import requests as req

# the emoji name, will be the key of the new emoji
# 表情包的名字，将会是新表情包的JSON键
emoji_name = "TG小黄鸭"

# the emoji data structure
# 表情包的数据结构
emoji_data = f'{{"{emoji_name}": {{ "type": "image", "container": []}}}}'
emoji_data = json.loads(emoji_data)

# the folder where the emoji images are stored
# 表情包图片存放的文件夹
folder = "UtyaDuck"

# the cdn url of the emoji images, end without slash /
# 表情包JSON的CDN地址，不要以斜杠结尾
cdn_url = "//raw.githubusercontent.com/SwaggyMacro/OwO_Stickers/main/stickers"

# url of the raw json file
# JSON文件的URL
owo_json_url = "https://raw.githubusercontent.com/SwaggyMacro/OwO_Stickers/main/OwO.min.json"

# the property where the new emoji data will be appended after, for example below is append after `TG小黄鸭`
# 新表情包数据将会被添加到的位置（比如以下是添加到`TG小黄鸭`的后面）
append_after = "TG小黄鸭"

# compress the json file
# 是否压缩JSON文件
need_compress = True

# get the json file
# 获取JSON文件
owo_json = req.get(owo_json_url).json()

for index, file  in enumerate(os.listdir(folder)):
    if file:
        emoji_data[emoji_name]["container"].append(
            {"text": f"{folder}-{index}", "icon":f"<img src='{cdn_url}/{folder}-Preview/{file}' "
                                                 f"origin='{cdn_url}/{folder}/{file}'>" ,})

for key, value in owo_json.items():
    if key == append_after:
        owo_json[key].update(emoji_data)
        break

if need_compress:
    file_content = json.dumps(owo_json, separators=(',', ':'), ensure_ascii=False)
else:
    file_content = json.dumps(owo_json, indent=4, ensure_ascii=False)

with open("OwO.min.json", "w", encoding="utf-8") as f:
    f.write(file_content)

print(file_content)