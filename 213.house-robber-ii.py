#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        case1 = basicRob(nums[1:-2]) + nums[len(nums) - 1]
        case2 = basicRob(nums[:-1])
        return max(case1, case2)


def basicRob(nums: List[int]) -> int:
    a = b = 0
    for n in nums:
        a, b = b, max(n+a, b)
    return b

# @lc code=end

# 74/74 cases passed (24 ms)
# Your runtime beats 96.79 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
