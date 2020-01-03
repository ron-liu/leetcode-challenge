#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start


# Solution 1: DFS
# Runtime: 236 ms, faster than 89.85% of Python3 online submissions for Jump Game III.
# Memory Usage: 19.3 MB, less than 100.00% of Python3 online submissions for Jump Game III.


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def can(arr: List[int], start: int, visited) -> bool:
            if start in visited or start < 0 or start > len(arr) - 1:
                return False
            if arr[start] == 0:
                return True
            visited.add(start)
            return can(arr, start - arr[start], visited) or can(arr, start + arr[start], visited)
        return can(arr, start, set())


# Solution 2: BFS
# Runtime: 232 ms, faster than 95.88% of Python3 online submissions for Jump Game III.
# Memory Usage: 19.1 MB, less than 100.00% of Python3 online submissions for Jump Game III.
# from queue import Queue
# class Solution:
#     def canReach(self, arr: List[int], start: int) -> bool:
#         visited = set()
#         queue = Queue()
#         queue.put(start)
#         while not queue.empty():
#             inx = queue.get()
#             if arr[inx] == 0:
#                 return True
#             visited.add(inx)
#             for x in [inx - arr[inx], inx + arr[inx]]:
#                 if x in visited or x <0 or x > len(arr) - 1:
#                     continue
#                 queue.put(x)
#         return False
