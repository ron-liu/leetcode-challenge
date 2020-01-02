#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start


class Solution:
    # Solution 1
    def moveZeroes(self, nums: List[int]) -> None:
        i, j, l = 0, 1, len(nums)
        while j < l and i < l:
            if nums[i] == 0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            else:
                i += 1
                j = max(i+1, j)

    # Solution 2
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     r = len(nums) -1
    #     l = 0

    #     while l < r:
    #         if nums[r] == 0:
    #             r -= 1
    #             continue
    #         if nums[l] == 0:
    #             nums[l:r] = nums[l+1: r + 1]
    #             nums[r] = 0
    #         else:
    #             l += 1

# @lc code=end

# solution 1
# 21/21 cases passed (52 ms)
# Your runtime beats 71.13 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.8 MB)

# solutin 2
# 21/21 cases passed (120 ms)
# Your runtime beats 16.57 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.9 MB)
