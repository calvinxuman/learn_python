#!/usr/bin/env python
# coding:utf-8
'''输出 9*9 乘法口诀表。'''
# def print_99_2():
#     #python2中的方法
#     for i in xrange(1,10):
#         for j in xrange(1,i+1):
#             print '%s * %s = %s\t'%(j,i,j*i) ,
#         print '\n' ,

def print_99_3():
    #python3中的方法
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s * %s = %s'%(j,i,j*i),end='\t')
        print('')

if __name__ == '__main__':
    # print_99_2()
    print_99_3()