#!/usr/bin/env python
# coding:utf-8
import copy

'''将一个列表的数据复制到另一个列表中。'''


def copy_list1(list):
    # 使用[:]方法copy
    list_copy = list[:]
    return list_copy


def copy_list2(list):
    # 使用append方法copy
    list_copy = []
    for i in list:
        list_copy.append(i)
    return list_copy


def copy_list3(list):
    # 使用列表自带的copy方法
    return copy.copy(list)


list_num = [1, 2, 3, 4, 5, 6, 7, 8]

print(copy_list1(list_num))
print(copy_list2(list_num))
print(copy_list3(list_num))
