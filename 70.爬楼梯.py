#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0]*(n+1)
        stairs[0] = 1
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(3, n+1):
                stairs[1] = 1
                stairs[2] = 2
                stairs[i] = stairs[i-1] + stairs[i-2]
            return stairs[n]
# @lc code=end
if __name__ == "__main__":
    n = 45
    a = Solution().climbStairs(n)
    print(a)
