#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        dummyHead = ListNode(-1, head) 
        cur = dummyHead 
        while cur.next: 
            if cur.next.val == val: 
                cur.next = cur.next.next 
            else: 
                cur = cur.next 
        return dummyHead.next
        
        # if head is None:
        #     return None
        # # if head.next is None and head.val != val:
        # #     return head
        

        # while True:
        #     if head.next.val == val:
        #         head == head.next.next
        #     else:
        #         head = head.next
        #     return head

# @lc code=end
