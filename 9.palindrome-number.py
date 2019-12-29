#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start


class Solution:
    # Solution 1
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y, cur = 0, x
        while cur > 0:
            y = y * 10 + cur % 10
            cur = cur // 10
        return y == x

    # Solution 2
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
    #     s,cur = [],x
    #     while cur > 0:
    #         s.append(cur % 10)
    #         cur = cur // 10
    #     l = len(s)
    #     if l <= 1:
    #         return True
    #     mid = (len(s) - 1) // 2
    #     left, right = (mid, mid+1) if l % 2 == 0 else (mid -1, mid + 1)
    #     while left >= 0 and right < l:
    #         if s[left] != s[right]:
    #             return False
    #         left = left - 1
    #         right = right + 1
    #     return True

# Solution 1
# 11509/11509 cases passed (56 ms)
# Your runtime beats 87.22 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# Solution 2
# Runtime: 80 ms, faster than 28.11% of Python3 online submissions for Palindrome Number.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Palindrome Number.


# @lc code=end
