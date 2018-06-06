#!/usr/bin/env python
#coding:utf-8
'''输入三个整数x,y,z，请把这三个数由小到大输出'''
nums = raw_input('请输入三个整数，用空格分隔(如65 38 45)：')
nums = nums.split(' ')

num_list = []
for i in nums:
    num_list.append(int(i))

def sortList(list):
    #定义一个排序函数
    for i in xrange(len(list)):
        for j in xrange(len(list)):
            if list[i] < list[j]:
                list[i],list[j] = list[j],list[i]
    return list

print('这三个数由小到大的顺序为：')
print(sortList(num_list))