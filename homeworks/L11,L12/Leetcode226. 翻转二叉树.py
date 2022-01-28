# -*- coding: utf-8 -*-
"""
@Time : 2022/1/28 18:10 
@Author : Zhi QIN 
@File : Leetcode226. 翻转二叉树.py 
@Software: PyCharm
@Brief : 18:19	info
			解答成功:
			执行耗时:52 ms,击败了11.12% 的Python3用户
			内存消耗:14.9 MB,击败了52.36% 的Python3用户
"""


# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
#
#
#
#  示例 1：
#
#
#
#
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
#
#
#  示例 2：
#
#
#
#
# 输入：root = [2,1,3]
# 输出：[2,3,1]
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
#  树中节点数目范围在 [0, 100] 内
#  -100 <= Node.val <= 100
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1157 👎 0

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

    # 递归
    def invertTree_(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    # 迭代
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
# leetcode submit region end(Prohibit modification and deletion)
