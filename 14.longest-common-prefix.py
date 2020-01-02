#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        ans, pos = '', 0
        while pos < len(strs[0]):
            equ = True
            for s in strs[1:]:
                if pos > len(s) - 1 or s[pos] != strs[0][pos]:
                    equ = False
                    break
            if equ:
                ans += strs[0][pos]
                pos += 1
            else:
                break

        return ans

# Runtime: 28 ms, faster than 92.98% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.

# @lc code=end
