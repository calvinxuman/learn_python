#!/usr/bin/env python
#coding:utf-8
'''企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%
提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成
3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发
放奖金总数？'''

def getBonus(i):
    bonus = 0
    if i <= 100000:
        bonus = i * 0.1
    elif 100000 < i <= 200000:
        bonus = 10000 + (i - 100000) * 0.075
    elif 200000 < i <= 400000:
        bonus = 10000 + 7500 + (i - 200000) * 0.05
    elif 400000 < i <= 600000:
        bonus = 10000 + 7500 + 10000 + (i - 400000) * 0.03
    elif 600000 < i <= 1000000:
        bonus = 10000 + 7500 + 10000 + 6000 + (i - 600000) * 0.015
    elif i > 1000000:
        bonus = 10000 + 7500 + 10000 + 6000 + 6000 + (i - 1000000) * 0.01
    return bonus

if __name__ == '__main__':
    i = raw_input('请输入利润：（单位：元）')
    if i.isdigit():
        bonus = getBonus(int(i))
        print('利润为%s元时，奖金为%s元'%(int(i),bonus))
    else:
        print('请输入正整数！')