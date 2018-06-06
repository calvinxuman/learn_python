#!/usr/bin/env python
# coding:utf-8
'''输入某年某月某日，判断这一天是这一年的第几天？'''


def isLeapYear(year):
    # 判断是否是闰年
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def isValidDate(year, month, day):
    # 判断日期是否合法
    month_31 = (1, 3, 5, 7, 8, 10, 12)
    if month > 12 or day > 31 or (month not in month_31 and day == 31):
        print('请输入正确的日期！')
        return False
    if (not isLeapYear(year) and month == 2 and day > 28) or (month == 2 and day > 29):
        print('2月不超过29天')
        return False
    else:
        return True


def calDate(year, month, day):
    # 计算具体某个日期为这一年的第多少天
    date_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date_num = 0
    for i in xrange(month - 1):
        date_num = date_num + date_list[i]
    if isLeapYear(year) and month > 2:
        return date_num + day + 1
    else:
        return date_num + day


if __name__ == '__main__':
    date = raw_input('请输入当前日期：（格式如：20180601）')
    if not date.isdigit() or len(date) != 8:
        print('您输入的日期格式不对!')
    else:
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
        if isValidDate(year, month, day):
            date_num = calDate(year, month, day)
            print('这一天是%s年的第%s天' % (year, date_num))
