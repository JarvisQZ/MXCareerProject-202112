# -*- coding: utf-8 -*-
"""
@Time : 2021/12/27 15:01 
@Author : Zhi QIN 
@File : Leetcode328. 奇偶链表.py 
@Software: PyCharm
@Brief : 15:09	info
			解答成功:
			执行耗时:44 ms,击败了32.83% 的Python3用户
			内存消耗:16.6 MB,击败了27.01% 的Python3用户
"""


# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
#  请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
#  示例 1:
#
#  输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
#
#
#  示例 2:
#
#  输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
#
#  说明:
#
#
#  应当保持奇数节点和偶数节点的相对顺序。
#  链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
#
#  Related Topics 链表 👍 513 👎 0

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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        prev = tail = head

        length = 1
        while tail.next:
            length += 1
            tail = tail.next

        n = length // 2

        while n > 0:
            post = prev.next
            tail.next = post
            tail = tail.next
            prev.next = post.next
            prev = prev.next
            post.next = None
            n -= 1
        return head

    # 力扣答案
    def oddEvenList_solution(self, head: ListNode) -> ListNode:
        if not head:
            return head

        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    head = p = ListNode(1)
    p.next = ListNode(2)
    p = p.next
    p.next = ListNode(3)
    p = p.next
    p.next = ListNode(4)
    p = p.next
    p.next = ListNode(5)

    s = Solution()
    res = s.oddEvenList(head)
    while res:
        print(res.val)
        res = res.next
