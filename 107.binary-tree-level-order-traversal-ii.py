#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
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

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def scan(node, level):
            if node is None: 
                return
            if len(ans) -1 < level:
                ans.append([])
            for sub in [node.left, node.right]:
                if sub is not None:
                    scan(sub, level+1)
            ans[level].append(node.val)
        scan(root, 0)
        ans.reverse()
        return ans
        
        
        
# @lc code=end

