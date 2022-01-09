# -*- coding: utf-8 -*-
"""
@Time : 2022/1/9 13:38 ->
@Author : Zhi QIN 
@File : 4-最小覆盖子串.py 
@Software: PyCharm
@Brief :

给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：
输入：s = "a", t = "a"
输出："a"
示例 3:
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
"""

from collections import defaultdict


def zui_xiao_fu_gai_zi_chuan(s, t):
    if len(t) > len(s):
        return ''

    need, window = defaultdict(int), defaultdict(int)
    for char in t:
        need[char] += 1

    left, right = 0, 0
    valid = 0
    start = 0
    length = len(s) + 1

    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        while valid == len(need):
            if right - left < length:
                start = left
                length = right - left

            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return "".join(s[start:start + length]) if length < len(s) else ''


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(zui_xiao_fu_gai_zi_chuan(s, t))
