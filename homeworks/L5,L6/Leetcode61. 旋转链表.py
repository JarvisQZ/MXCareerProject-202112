# -*- coding: utf-8 -*-
"""
@Time : 2021/12/27 14:31 
@Author : Zhi QIN 
@File : Leetcode61. 旋转链表.py 
@Software: PyCharm
@Brief : 14:31	info
			解答成功:
			执行耗时:36 ms,击败了73.18% 的Python3用户
			内存消耗:15 MB,击败了31.08% 的Python3用户
"""

# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#
#
#  示例 2：
#
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
#
#
#  提示：
#
#
#  链表中节点的数目在范围 [0, 500] 内
#  -100 <= Node.val <= 100
#  0 <= k <= 2 * 10⁹
#
#  Related Topics 链表 双指针 👍 689 👎 0
from typing import Optional


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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-1, head)
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        if k % length == 0:
            return head
        k = k % length
        p = head
        for i in range(length - k - 1):
            p = p.next
        dummy.next = p.next
        q = p
        for i in range(k):
            q = q.next
        q.next = head
        p.next = None

        return dummy.next

    # 答案
    def rotateRight_solution(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        if (add := n - k % n) == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret

# leetcode submit region end(Prohibit modification and deletion)
