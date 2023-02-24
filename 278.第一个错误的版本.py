#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        if n == 1:
            return 1

        while right - left > 1:
            if isBadVersion((left+right)//2):
                right = (left+right)//2
            if not isBadVersion((left+right)//2):
                left = (left+right)//2
        if isBadVersion(left):
            return left
        else:
            return right
# @lc code=end
