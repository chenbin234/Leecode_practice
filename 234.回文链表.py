#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        if head.next is None:
            return True
        res = [head.val]
        while head.next:
            res.append(head.next.val)
            head = head.next
        if res == res[::-1]:
            return True
        else:
            return False
# @lc code=end
