#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            else:
                high -= 1

# @lc code=end

# 17/17 cases passed (60 ms)
# Your runtime beats 93.62 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.3 MB)
