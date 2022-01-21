# -*- coding: utf-8 -*-
"""
@Time : 2022/1/21 17:07 
@Author : Zhi QIN 
@File : 剑指 Offer 13. 机器人的运动范围.py 
@Software: PyCharm
@Brief : 
"""

# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一
# 格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但
# 它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
#
#
#  示例 1：
#
#  输入：m = 2, n = 3, k = 1
# 输出：3
#
#
#  示例 2：
#
#  输入：m = 3, n = 1, k = 0
# 输出：1
#
#
#  提示：
#
#
#  1 <= n,m <= 100
#  0 <= k <= 20
#
#  Related Topics 深度优先搜索 广度优先搜索 动态规划 👍 394 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def digits_sum(n):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res

        visited = set()

        def dfs(i, j):
            if i >= m or j >= n or digits_sum(i) + digits_sum(j) > k or (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i, j + 1)

        dfs(0, 0)
        return len(visited)
    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    S = Solution()
    print(S.movingCount(3, 2, 17))
