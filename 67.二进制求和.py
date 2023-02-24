#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_dec = int(a,2)
        b_dec = int(b,2)
        c = a_dec + b_dec
        return bin(c)[2:]
# @lc code=end
