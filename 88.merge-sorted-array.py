#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n-1, m+n-1
        while i >= 0 and j >= 0:
            A[k] = max(A[i], B[j])
            if A[i] > B[j]:
                i = i - 1
            else:
                j = j-1
            k = k - 1
        if i < 0:
            for l in range(0, j+1):
                A[l] = B[l]


# @lc code=end

# 59/59 cases passed (28 ms)
# Your runtime beats 98.21 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
