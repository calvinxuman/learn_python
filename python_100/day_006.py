#!/usr/bin/env python
#coding:utf-8
'''斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
定义一个斐波那契数列函数，使之传入参数n，返回第n个斐波那契数'''

def fib(n):
    #使用递归函数
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fibna(n):
    #使用生成器函数
    a,b = 0,1
    while n > 0:
        yield a
        a, b = b, a + b
        n = n-1

print(fib(10))
print('-----------------------')
for i in fibna(10):
    print(i)