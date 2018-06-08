#!/usr/bin/env python
# coding:utf-8
import json
import time

'''利用python脚本修改海南三期中最近24小时dns解析趋势'''
with open(r'../test_data/get_24_trend_chart.json') as json_file:
    json_data = json.load(json_file)
print(json_data[0]['time'])

def getNowHour():
    date = time.strftime("%Y-%m-%d",time.localtime())
    hour = time.strftime("%H",time.localtime())
    return date,hour
print(getNowHour())

