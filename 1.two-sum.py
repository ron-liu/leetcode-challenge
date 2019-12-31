#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, val in enumerate(nums):
            match = target - nums[i]
            if match not in dict:
                dict[val] = i
                continue
            return [i, dict[match]]

# @lc code=end
# 29/29 cases passed (40 ms)
# Your runtime beats 98.96 % of python3 submissions
# Your memory usage beats 65.81 % of python3 submissions (14 MB)
