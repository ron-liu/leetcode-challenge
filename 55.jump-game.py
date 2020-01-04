#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
# DFS from back
# Runtime: 96 ms, faster than 43.98% of Python3 online submissions for Jump Game.
# Memory Usage: 42.1 MB, less than 7.14% of Python3 online submissions for Jump Game.
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         visited = {0: True}
#         def can(nums: List[int], pos) -> bool:
#             if pos in visited:
#                 return visited[pos]
#             for i in range(pos-1, -1, -1):
#                 if nums[i] >= pos - i:
#                     if can(nums, i):
#                         visited[i] = True
#                         return True
#                     else:
#                         visited[i] = False
#             return False
#         return can(nums, len(nums) - 1)

# I dont know why it exceeds time
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         goods = {len(nums)-1}
#         for i in range(len(nums) - 2, -1, -1):
#             for j in range(i+1, min(len(nums), nums[i] + i + 1)):
#                 if j in goods:
#                     goods.add(i)
#         return 0 in goods


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0


# @lc code=end
# 75/75 cases passed (80 ms)
# Your runtime beats 98.55 % of python3 submissions
# Your memory usage beats 11.9 % of python3 submissions (14.7 MB)
