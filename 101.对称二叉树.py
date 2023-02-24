#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def check(self, p, q):
    #     if p.val != q.val:
    #         return False
    #     else:
    #         return self.check(p.left, q.right) and self.check(p.right, q.left)


    def check(self,left: TreeNode,right: TreeNode):
        #递归的终止条件是两个节点都为空
        #或左右有任意一个不为空，一定不对称
        #两个节点的值不相等
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        
        return self.check(left.left,right.right) and self.check(left.right,right.left)



    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False
        else:
            return self.check(root.left, root.right)


# @lc code=end
