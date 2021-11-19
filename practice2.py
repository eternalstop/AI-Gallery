# -*- coding: utf8 -*-
# code by ali
"""
简单的加法

题目描述
输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字。
如果有多对数字的和等于输入的数字，输出任意一对即可。
例如：输入数组1 2 4 7 11 15和数字15。
由于4+11=15，因此输出4和11。
"""
l = input()  # 输入字符串，以空格为间隔，请自行实现将字符串转换为数组的代码
# l = "1 2 4 7 11 15"
n = input()  # 输入数字
# n = "15"


def func():
    # 在此编写代码
    # 根据空格切割成列表
    tmp_list = l.split()
    # 列表长度
    list_len = len(tmp_list)
    # 双循环遍历元素相加
    for a in range(0, list_len, 1):
        for b in range(a+1, list_len, 1):
            # 判断和是否等于指定数值
            if int(tmp_list[a]) + int(tmp_list[b]) == int(n):
                # 输出符合条件的元素
                print(tmp_list[a], tmp_list[b])
                # return函数结束，跳出循环
                return
            else:
                # 不符合条件时继续遍历
                continue
        # 当循环到最后一个元素时还没有符合条件的数值输出Nothing
        if a == list_len - 1:
            print("Nothing")
            return


func()
