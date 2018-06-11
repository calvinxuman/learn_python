#!/usr/bin/env python
# coding:utf-8
import json
import time
import random

'''利用python脚本修改海南三期中最近24小时dns解析趋势,和总的dns解析量'''

def getTime():
    #获取最近24小时时间列表
    time_list = []
    for i in xrange(1,25):
        date = time.strftime("%Y-%m-%d %H",time.localtime(time.time()-3600*i))
        hour = date + ':00'
        time_list.append(hour)
    return time_list

def getAmount():
    #随机获取每小时dns解析量
        return random.randint(500,700)

def load_file(file):
    #读取json文件
    with open(file) as f:
        return json.load(f)

def write_file(data,file):
    #将json数据写入文件
        with open(file,'w') as f:
            f.write(json.dumps(data))

def update_24json(data):
    #更新24小时json文件中的时间
    json_time = getTime()
    for i in xrange(len(json_data)):
        json_data[i]["parse_amount"] = getAmount()
        json_data[i]["parse_suc"] = json_data[i]["parse_amount"] - random.randint(0,20)
        json_data[i]["suc_rate"] = round(100*json_data[i]["parse_suc"]/float(json_data[i]["parse_amount"]),2)
        json_data[i]["time"] = json_time[i]

def update_dns(data_24,data_total):
    #更新总dns解析json文件
    all_count = 0
    succ_count = 0
    for i in data_24:
        all_count += i['parse_amount']
        succ_count += i['parse_suc']
    suc_rate = round(100*succ_count/float(all_count),2)
    data_total['all_count'], data_total['succ_count'], data_total['suc_rate'] = all_count, succ_count, suc_rate

if __name__ == '__main__':
    trend_24 = r'./dnsParse/get_24_trend_chart.json'
    dns_parse = r'./dnsParse/get_parse_situation.json'
    json_data = load_file(trend_24)
    update_24json(json_data)
    write_file(json_data,trend_24)
    dns_json = load_file(dns_parse)
    update_dns(json_data,dns_json)
    write_file(dns_json,dns_parse)
