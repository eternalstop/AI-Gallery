# -*- coding: utf8 -*-
# code by ali
"""
逆序除重

题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。 保证输入的整数最后一位不是0。
输入描述： 输入一个int型整数
输出描述： 按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
示例1 输入： 30010733 输出： 3701
"""

num = input()

try:
    int(num)
    num_list = list(num)
    if num_list[-1] != '0':
        num_list.reverse()
        res_list = list(set(num_list))
        res_list.sort(key=num_list.index)
        res = ''.join(res_list)
        print(res)
    else:
        print("请输入一个不以0结尾的整数")
except:
    print("请输入一个整数")

