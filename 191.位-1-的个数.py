#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = ("0"*32+bin(n)[2:])[-32:]
        res = 0
        for i in range(32):
            res = res + int(n[i])
        return res
        
# @lc code=end
