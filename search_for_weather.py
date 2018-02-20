#-*_coding:utf-8-*-
import json
import urllib.request
import sys
sys.path.append('F:/pythonSaver/code_of_city.py')
import code_of_city

city is city
cityname=input('你想查哪个城市的天气?\n')
citycode=city.get('城市代码')      #暂作更改,记得改回
if citycode:
    url=(
        'http://www.weather.com.cn/data/cityinfo/%s.html'
     %citycode)
    content=urllib.request.urlopen(url).read()
    print(content)
