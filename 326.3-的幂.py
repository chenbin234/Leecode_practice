#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 or n == 2:
            return False
        if n == 1:
            return True
        while n >= 2:
            if n % 3 != 0:
                return False
            else:
                n = n/3
        return True
# @lc code=end
