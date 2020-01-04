#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i].reverse()
        return ans


# Runtime: 28 ms, faster than 83.20% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
:

    # @lc code=end
