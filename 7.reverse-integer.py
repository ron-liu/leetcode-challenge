#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        prefix = '' if x >= 0 else '-'
        ret = int(prefix + str(abs(x))[::-1])
        return ret if -2 ** 31 <= ret and ret <= 2**31 - 1 else 0


# @lc code=end

# 1032/1032 cases passed (28 ms)
# Your runtime beats 88.64 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
