#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = q = 0
        while p < len(s) and q < len(t):
            if t[q] == s[p]:
                p += 1
            q += 1
        return p == len(s)

# @lc code=end

# 14/14 cases passed (308 ms)
# Your runtime beats 6.48 % of python3 submissions
# Your memory usage beats 26.67 % of python3 submissions (17.1 MB)
