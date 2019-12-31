#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        setPos, readPos = 0, 2
        while True:
            if nums[setPos] != nums[setPos + 1]:
                setPos += 1
            if readPos < len(nums):
                nums[setPos + 1] = nums[readPos]
                readPos += 1
            else:
                break
        return setPos + 1


# @lc code=end

# 161/161 cases passed (84 ms)
# Your runtime beats 88.32 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.3 MB)
