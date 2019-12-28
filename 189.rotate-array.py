#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[length - k:] + nums[:length - k]

# Accepted
# 34/34 cases passed (64 ms)
# Your runtime beats 78.28 % of python3 submissions
# Your memory usage beats 5.09 % of python3 submissions (14.1 MB)
