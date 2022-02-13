# -*- coding: utf-8 -*-
"""
@Time : 2022/2/13 13:04 
@Author : Zhi QIN 
@File : quiz_03_秦至.py
@Software: PyCharm
@Brief :
"""


# 1. 最短无序连续子数组
#
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 请你找出符合题意的 最短 子数组，并输出它的长度。
#
# 示例 1：
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
# 示例 2：
# 输入：nums = [1,2,3,4]
# 输出：0
#
# 示例 3：
# 输入：nums = [1]
# 输出：0

def shortest_unordered_list(nums):
    length = len(nums)
    if length < 2:
        return 0

    left, right = 0, length - 1

    while left < right:
        if nums[left] < nums[left + 1]:
            left += 1
        if nums[right] > nums[right - 1]:
            right -= 1

        if nums[left] > nums[left + 1] and nums[right] < nums[right - 1]:
            break

    return right - left + 1


# 2. 搜索二维矩阵
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#
# 示例 1：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#
# 示例 2：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false

"""
[[ 1, 3, 5, 7],
 [10,11,16,20],
 [23,30,34,60]]
"""


def search_in_2d_matrix(matrix, target):
    height = len(matrix)
    width = len(matrix[0])

    i, j = 0, width - 1

    while i < height and j >= 0:
        if matrix[i][j] > target:
            i += 1
        if matrix[i][j] < target:
            j -= 1
        else:
            return True
    return False


# 3. 将二叉搜索树变平衡
#
# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。
# 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
# 如果有多种构造方法，请你返回任意一种。
#
# 输入（层序遍历）：root = [1,null,2,null,3,null,4,null,null]
# 输出（层序遍历）：[2,1,3,null,null,null,4]
# 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
#
# 提示：
# 树节点的数目在 1 到 10^4 之间。
# 树节点的值互不相同，且在 1 到 10^5 之间。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balance_bst(root):
    pass
    # inorder_list = []
    #
    # def inorder(node):
    #     if node.left:
    #         inorder(node.left)
    #
    #     inorder_list.append(node.value)
    #
    #     if node.right:
    #         inorder(node.right)
    #
    # def build_bst(left, right):
    #     mid = (left + right) // 2
    #     node = TreeNode(inorder_list[mid])
    #     if left <= mid - 1:
    #         node.left = build_bst(left, mid - 1)
    #     if mid + 1 <= right:
    #         node.right = build_bst(mid + 1, right)
    #
    #     return node
    #
    # inorder(root)
    # return build_bst(0, len(inorder_list) - 1)


if __name__ == '__main__':
    # q1 #

    # nums = [2, 6, 4, 8, 10, 9, 15]
    nums = [1, 2, 3, 4]
    print(shortest_unordered_list(nums))

    #######################################################################
    # q2 #
    # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # target = 3

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13

    print(search_in_2d_matrix(matrix=matrix, target=target))

    #######################################################################
    # q3 #
