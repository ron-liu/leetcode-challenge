#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        far, close = 1, 1
        for i in range(1, n):
            far, close = close, far + close
        return close

# @lc code=end

# 45/45 cases passed (20 ms)
# Your runtime beats 98.3 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
