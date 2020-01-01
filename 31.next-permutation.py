#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:

                # binary search to find the next bigger one in the list whose index starts from i + 1
                low, high = i + 1, len(nums) - 1
                while low < high:
                    mid = (high + low) // 2
                    if nums[mid] > nums[i]:
                        low = mid + 1
                    else:
                        high = mid - 1
                j = low - 1 if nums[low] <= nums[i] else low

                # swap
                nums[i], nums[j] = nums[j], nums[i]

                # order it
                nums[i+1:] = sorted(nums[i+1:])
                return
        nums.sort()

# @lc code=end

# 265/265 cases passed (40 ms)
# Your runtime beats 82.81 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
