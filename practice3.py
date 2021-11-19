# -*- coding: utf8 -*-
# code by ali
"""
字符串作业

题目描述
输入一个字符串，求最大的没有重复字符的子字符串长度
比如：输入huaweicloudaigallery
输出
9 （huaweiclo或aweicloud或weiclouda）
"""
string = input()  # 手动输入字符串


def func():
    str_list = list(string)
    # store all the sublists
    max_list = [[]]

    for i in range(1, len(str_list) + 1):
        for j in range(i + 1, len(str_list) + 1):
            # slice the subarray
            sub = str_list[i:j]
            max_list.append(sub)
    return len(max_list)

func()
