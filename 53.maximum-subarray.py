#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start, sum, ret = 0, 0, -sys.maxsize
        for pos, val in enumerate(nums):
            sum = max(sum+val, val)
            ret = max(ret, sum)
        return ret

# @lc code=end

# 202/202 cases passed (72 ms)
# Your runtime beats 62.94 % of python3 submissions
# Your memory usage beats 86.18 % of python3 submissions (13.5 MB)
