# -*- coding: utf-8 -*-
"""
@Time : 2021/12/22 13:58 
@Author : Zhi QIN 
@File : Leetcode151. 翻转字符串里的单词.py 
@Software: PyCharm
@Brief : 
"""
# 给你一个字符串 s ，逐个翻转字符串中的所有 单词 。
#
#  单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
#
#  请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。
#
#  说明：
#
#
#  输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
#  翻转后单词间应当仅用一个空格分隔。
#  翻转后的字符串中不应包含额外的空格。
#
#
#
#
#  示例 1：
#
#
# 输入：s = "the sky is blue"
# 输出："blue is sky the"
#
#
#  示例 2：
#
#
# 输入：s = "  hello world  "
# 输出："world hello"
# 解释：输入字符串可以在前面或者后面包含多余的空格，但是翻转后的字符不能包括。
#
#
#  示例 3：
#
#
# 输入：s = "a good   example"
# 输出："example good a"
# 解释：如果两个单词间有多余的空格，将翻转后单词间的空格减少到只含一个。
#
#
#  示例 4：
#
#
# 输入：s = "  Bob    Loves  Alice   "
# 输出："Alice Loves Bob"
#
#
#  示例 5：
#
#
# 输入：s = "Alice does not even like bob"
# 输出："bob like even not does Alice"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10⁴
#  s 包含英文大小写字母、数字和空格 ' '
#  s 中 至少存在一个 单词
#
#
#
#
#
#
#
#  进阶：
#
#
#  请尝试使用 O(1) 额外空间复杂度的原地解法。
#
#  Related Topics 双指针 字符串 👍 419 👎 0

# python 和 Java 字符串无法原地

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

# leetcode submit region end(Prohibit modification and deletion)
