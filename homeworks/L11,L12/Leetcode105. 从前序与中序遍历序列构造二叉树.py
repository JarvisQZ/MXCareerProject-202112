# -*- coding: utf-8 -*-
"""
@Time : 2022/1/28 18:01 
@Author : Zhi QIN 
@File : Leetcode105. 从前序与中序遍历序列构造二叉树.py 
@Software: PyCharm
@Brief : 18:10	info
			解答成功:
			执行耗时:144 ms,击败了38.41% 的Python3用户
			内存消耗:88.6 MB,击败了5.01% 的Python3用户
"""

# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并
# 返回其根节点。
#
#
#
#  示例 1:
#
#
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
#
#
#  示例 2:
#
#
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#
#
#
#
#  提示:
#
#
#  1 <= preorder.length <= 3000
#  inorder.length == preorder.length
#  -3000 <= preorder[i], inorder[i] <= 3000
#  preorder 和 inorder 均 无重复 元素
#  inorder 均出现在 preorder
#  preorder 保证 为二叉树的前序遍历序列
#  inorder 保证 为二叉树的中序遍历序列
#
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 1395 👎 0
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return

        root_val = preorder[0]
        root = TreeNode(root_val)

        sep_idx = inorder.index(root_val)

        inorder_left = inorder[:sep_idx]
        inorder_right = inorder[sep_idx + 1:]

        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        root.left = self.buildTree(preorder=preorder_left, inorder=inorder_left)
        root.right = self.buildTree(preorder=preorder_right, inorder=inorder_right)

        return root

# leetcode submit region end(Prohibit modification and deletion)
