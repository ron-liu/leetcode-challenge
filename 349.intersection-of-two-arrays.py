#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start


class Solution:
    def intersection(self, A: List[int], B: List[int]) -> List[int]:
        m, n = len(A), len(B)
        if m > n:
            m, n, A, B = n, m, B, A
        bset = set()
        ret = set()
        for val in B:
            bset.add(val)
        for val in A:
            if val in bset:
                ret.add(val)
        return list(ret)

# @lc code=end

# 60/60 cases passed (44 ms)
# Your runtime beats 87.09 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
