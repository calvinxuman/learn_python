#!/usr/bin/env python
# coding:utf-8
import json
import time

'''利用python脚本修改海南三期中最近24小时dns解析趋势'''
with open(r'../test_data/get_24_trend_chart.json') as json_file:
    json_data = json.load(json_file)
# print(json_data[0]['time'])

def getTime():
    time_list = []
    for i in xrange(25):
        date = time.strftime("%Y-%m-%d %H",time.localtime(time.time()-3600*i))
        hour = date + ':00'
        time_list.append(hour)
    return time_list

if __name__ == '__main__':
    json_time = getTime()
    for i in xrange(len(json_data)):
        json_data[i]["time"] = json_time[i]
    with open(r'../test_data/new_get_24_trend_chart.json','w') as new_file:
        new_file.write(json.dumps(json_data))
