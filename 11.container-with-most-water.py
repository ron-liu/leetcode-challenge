#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        i, j, ans = 0, len(height) - 1, 0
        while i != j:
            ans = max(getArea(height, i, j), ans)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans


def getArea(heights: List[int], i, j) -> int:
    return (j-i) * min(heights[i], heights[j])
# @lc code=end
# 50/50 cases passed (140 ms)
# Your runtime beats 56.39 % of python3 submissions
# Your memory usage beats 68.42 % of python3 submissions (14.4 MB)
