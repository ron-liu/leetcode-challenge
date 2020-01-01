#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums) // 2
        dict = {}
        for n in nums:
            times = dict.get(n, 0)
            if times >=  half:
                return n
            dict[n] = times + 1
        
# @lc code=end

# 44/44 cases passed (192 ms)
# Your runtime beats 53.35 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.1 MB)