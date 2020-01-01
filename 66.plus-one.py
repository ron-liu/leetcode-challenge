#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
# Solution 1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curry, pos = 1, len(digits) - 1
        while curry == 1 and pos >= 0:
            if digits[pos] == 9:
                curry = 1
                digits[pos] = 0
            else:
                curry = 0
                digits[pos] += 1
            pos -= 1
        return [1] + digits if curry == 1 else digits

# Solution 2
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         curry, pos = 1, len(digits) - 1
#         while curry == 1 and pos >= 0:
#             digits[pos] = (digits[pos] + 1) % 10
#             curry = 1 if digits[pos] == 0 else 0
#             pos -= 1
#         return [1] + digits if curry == 1 else digits

# @lc code=end

# Solution 1
# 109/109 cases passed (28 ms)
# Your runtime beats 88.94 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)

#Solution 2
# 109/109 cases passed (32 ms)
# Your runtime beats 71.06 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)