#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
# BFS
# Runtime: 104 ms, faster than 44.30% of Python3 online submissions for Jump Game II.
# Memory Usage: 15 MB, less than 8.33% of Python3 online submissions for Jump Game II.
# from queue import Queue
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         farest,steps, i  = 0, 0, 0
#         while i < len(nums):
#             newFarest = farest
#             for j in range(i, farest + 1 ):
#                 newFarest = max(newFarest, nums[j] + j)
#                 if newFarest >= len(nums) -1:
#                     return steps + 1
#             if newFarest > farest:
#                 steps += 1
#                 i = farest + 1
#                 farest = newFarest

# 92/92 cases passed (104 ms)
# Your runtime beats 44.3 % of python3 submissions
# Your memory usage beats 8.33 % of python3 submissions (15 MB)


class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end, steps = 0, 0, 0
        while end < len(nums) - 1:
            steps += 1
            newEnd = end
            for i in range(start, end + 1):
                newEnd = max(newEnd, nums[i] + i)
                if newEnd >= len(nums) - 1:
                    return steps
            start = end + 1
            end = newEnd

        return steps


# @lc code=end
