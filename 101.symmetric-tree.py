#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
from queue import Queue


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left, right) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        return isMirror(root, root)


# @lc code=end
