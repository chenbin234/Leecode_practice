#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        if root is None:
            return 0
        elif root.left is None or root.right is None:
            left_height = self.minDepth(root.left)
            right_height = self.minDepth(root.right)
            return max(left_height,right_height) + 1
        else:
            left_height = self.minDepth(root.left)
            right_height = self.minDepth(root.right)
        return min(left_height,right_height) + 1
# @lc code=end
