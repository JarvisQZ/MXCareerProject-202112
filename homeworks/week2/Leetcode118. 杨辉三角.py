# -*- coding: utf-8 -*-
"""
@Time : 2021/12/22 13:58 
@Author : Zhi QIN 
@File : Leetcode118. 杨辉三角.py 
@Software: PyCharm
@Brief : 
"""
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
#  在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
#
#
#
#
#  示例 1:
#
#
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#
#  示例 2:
#
#
# 输入: numRows = 1
# 输出: [[1]]
#
#
#
#
#  提示:
#
#
#  1 <= numRows <= 30
#
#  Related Topics 数组 动态规划 👍 651 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

# [0123]
# [1230]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[] for _ in range(numRows)]
        res[0] = [1]
        # while len(res) < numRows:
        #     new_row = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
        #     res.append(new_row)
        for i in range(1, numRows):
            new_row = [a+b for a,b in zip(res[i-1]+[0], [0]+res[i-1])]
            res[i] = new_row
        return res

# leetcode submit region end(Prohibit modification and deletion)
