#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):

        # def compare2nodes(nodeA,nodeB):
        #     if nodeA == nodeB:
        #         return nodeA
        #     elif nodeA != nodeB and nodeB.next is not None:
        #         return compare2nodes(nodeA,nodeB.next)
        #     else:
        #         return None

        # a = compare2nodes(headA,headB)
        # if a is not None:
        #     return a
        # elif a is None and headA.next is not None:
        #     headA = headA.next
        #     a = compare2nodes(headA,headB)
        # else:
        #     return None
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

# @lc code=end