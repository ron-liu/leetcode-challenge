#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for n in nums:
            a, b = b, max(a+n, b)
        return b


# @lc code=end
# 69/69 cases passed (28 ms)
# Your runtime beats 86.83 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
