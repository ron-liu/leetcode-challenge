#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
# Runtime: 40 ms, faster than 15.07% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
# from queue import Queue
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#             return []
#         q = Queue()
#         q.put(root)
#         ans = []
#         while not q.empty():
#             arr = []
#             while not q.empty():
#                 arr.append(q.get())
#             ans.append(list(map(lambda x:x.val, arr)))
#             for node in arr:
#                 for subNode in [node.left, node.right]:
#                     if subNode is not None:
#                         q.put(subNode)
#         return ans
            
# DFS
# Runtime: 32 ms, faster than 73.09% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13.3 MB, less than 77.42% of Python3 online submissions for Binary Tree Level Order Traversal.
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def scan(root, level):
            if root is None:
                return
            if len(ans) - 1 < level:
                ans.append([])
            ans[level].append(root.val)
            scan(root.left, level+1)
            scan(root.right, level+1)
        scan(root, 0)
        return ans
        
        
# @lc code=end

