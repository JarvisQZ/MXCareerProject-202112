# -*- coding: utf-8 -*-
"""
@Time : 2021/12/27 13:52 
@Author : Zhi QIN 
@File : Leetcode203. 移除链表元素.py 
@Software: PyCharm
@Brief : 13:51	info
        解答成功:
        执行耗时:60 ms,击败了56.30% 的Python3用户
        内存消耗:17.9 MB,击败了72.59% 的Python3用户
"""


# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
#
#
#  示例 1：
#
#
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
#
#
#  示例 2：
#
#
# 输入：head = [], val = 1
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
#
#
#
#
#  提示：
#
#
#  列表中的节点数目在范围 [0, 10⁴] 内
#  1 <= Node.val <= 50
#  0 <= val <= 50
#
#  Related Topics 递归 链表 👍 763 👎 0

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        p = head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head if head.val != val else head.next

# leetcode submit region end(Prohibit modification and deletion)
