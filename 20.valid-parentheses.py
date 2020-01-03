#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        opens = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                d = stack.pop()
                if c != opens.get(d):
                    return False
        return len(stack) == 0


# Runtime: 20 ms, faster than 97.80% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.

# @lc code=end
