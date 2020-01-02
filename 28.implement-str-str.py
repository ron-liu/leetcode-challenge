#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

# @lc code=end

# 74/74 cases passed (28 ms)
# Your runtime beats 85.75 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
