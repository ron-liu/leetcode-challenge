#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        start, end = -1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                if (nums[mid - 1] != target if mid > 0 else True):
                    start = mid
                    break
                else:
                    hi = mid - 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if start == -1:
            return [start, end]

        if (nums[start + 1] != target if start < len(nums) - 1 else True):
            return [start, start]

        lo, hi = start + 1, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                if (nums[mid + 1] != target if mid < len(nums) - 1 else True):
                    end = mid
                    break
                else:
                    lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return [start, end]

# @lc code=end
# 88/88 cases passed (84 ms)
# Your runtime beats 94.18 % of python3 submissions
# Your memory usage beats 5.36 % of python3 submissions (14.1 MB)
