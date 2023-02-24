#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while True:
            n = n + 1
            number = n*n 
            if number > x:
                break
        return n-1

# @lc code=end

if __name__ == "__main__":
    x = 4
    a = Solution().mySqrt(x)
    print(a)