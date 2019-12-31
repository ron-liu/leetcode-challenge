#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        for i, v in enumerate(nums):
            if v != val:
                nums[pos] = v
                pos += 1
        return pos

# @lc code=end
# 113/113 cases passed (24 ms)
# Your runtime beats 98.06 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
