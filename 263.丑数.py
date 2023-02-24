#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factor = [2,3,5]
        for i in factor:
            while n % i == 0:
                n = n // i
        return n == 1
# @lc code=end
if __name__ == "__main__":
    n = 7
    a = Solution().isUgly(n)
    print(a)