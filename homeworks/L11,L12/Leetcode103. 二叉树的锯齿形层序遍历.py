# -*- coding: utf-8 -*-
"""
@Time : 2022/1/28 18:49 
@Author : Zhi QIN 
@File : Leetcode103. 二叉树的锯齿形层序遍历.py 
@Software: PyCharm
@Brief : 
"""

# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
#
#
#  示例 2：
#
#
# 输入：root = [1]
# 输出：[[1]]
#
#
#  示例 3：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [0, 2000] 内
#  -100 <= Node.val <= 100
#
#  Related Topics 树 广度优先搜索 二叉树 👍 581 👎 0
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        # 双端队列
        from collections import deque

        queue = deque([root])
        count = 0

        while queue:
            nodes = []
            temp = []
            while queue:
                temp.append(queue[0].val)
                nodes.append(queue.popleft())
            res.append(temp) if count % 2 == 0 else res.append(temp[::-1])
            count += 1
            for node in nodes:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

# leetcode submit region end(Prohibit modification and deletion)
