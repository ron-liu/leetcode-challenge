#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
import sys


class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        # i means A(1...i-1) belongs to left part, i is (0...m) both inclusive
        # j means B(1...j-1) belongs to left part, j is (0...n) both inclusive
        # i + j = (m + n) // 2
        low, high = 0, m
        while True:
            i = (low + high) // 2
            j = (m + n) // 2 - i
            if low == high:
                break
            if min(self.pos(A, i, sys.maxsize), self.pos(B, j, sys.maxsize)) >= max(self.pos(A, i - 1, -sys.maxsize), self.pos(B,  j - 1, -sys.maxsize)):
                break
            if self.pos(A, i, -sys.maxsize) < self.pos(B, j - 1, -sys.maxsize):
                low, high = i + 1, high
            else:
                low, high = low, i - 1
        if (m + n) % 2 == 0:
            return (max(self.pos(A, i-1, -sys.maxsize), self.pos(B, j-1, -sys.maxsize)) + min(self.pos(A, i, sys.maxsize), self.pos(B, j, sys.maxsize))) / 2
        else:
            return min(self.pos(A, i, sys.maxsize), self.pos(B, j, sys.maxsize))

    def pos(self, list: List[int], i: int, default: int) -> int:
        return default if i >= len(list) or i < 0 else list[i]

# @lc code=end

# 2085/2085 cases passed (92 ms)
# Your runtime beats 91.41 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)


""" Test cases
[1]
[2,3]

[1,1]
[1,2]

[]
[1,2]

[]
[1,2,3,4,5]

[1,3]
[2]

[1,2]
[3,4]

[0,0]
[0,0]
"""
