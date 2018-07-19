# coding:utf-8
# 获取车站信息并进行解析，储存为字典:https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9059

import re
import requests
import urllib
from urllib.request import urlopen
from urllib.parse import urlencode
from pprint import pprint



# # 读取数据：
# url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9059'
# r = urllib.request.urlopen(url)
# r_content = r.read().decode('utf-8')
# # print(r_content)
# # pprint(r_content)
# #
# # 将数据储存为字典形式：
# # 匹配中文和对应的英文：
# stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', r_content)
# stations1 = dict(stations)
# # 转化成字典形式：
# station_names = dict(zip(stations1.keys(), stations1.values()))
# # pprint(station_name)
# print(station_names)


# 使用requests方法：
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9059'
r = requests.get(url)
# print(r.text)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', r.text)
stations1 = dict(stations)

# pprint(stations1.keys())
# pprint(stations1.values())

station_names = dict(zip(stations1.keys(), stations1.values()))
pprint(station_names)

# 储存字典：
f = open('station_names.txt', 'w')
f.write(str(station_names))
f.close()



















