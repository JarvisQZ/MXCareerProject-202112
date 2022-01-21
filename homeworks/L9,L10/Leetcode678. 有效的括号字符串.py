# -*- coding: utf-8 -*-
"""
@Time : 2022/1/21 16:01 
@Author : Zhi QIN 
@File : Leetcode678. 有效的括号字符串.py 
@Software: PyCharm
@Brief : 
"""

# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
#
#
#  任何左括号 ( 必须有相应的右括号 )。
#  任何右括号 ) 必须有相应的左括号 ( 。
#  左括号 ( 必须在对应的右括号之前 )。
#  * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
#  一个空字符串也被视为有效字符串。
#
#
#  示例 1:
#
#
# 输入: "()"
# 输出: True
#
#
#  示例 2:
#
#
# 输入: "(*)"
# 输出: True
#
#
#  示例 3:
#
#
# 输入: "(*))"
# 输出: True
#
#
#  注意:
#
#
#  字符串大小将在 [1，100] 范围内。
#
#  Related Topics 栈 贪心 字符串 动态规划 👍 439 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right = 0, 0
        s_list = list(s)
        for char in s_list:
            if char == '(':
                left += 1
                right += 1
            elif char == ')':
                left -= 1
                right -= 1
            else:
                left -= 1
                right += 1
            left = max(left, 0)
            if left > right:
                return False
        return left == 0

# leetcode submit region end(Prohibit modification and deletion)
