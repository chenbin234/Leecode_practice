#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:   
        if num <= 9:
            return num
        while num > 9:
            sum = 0
            num = str(num)
            for i in num:
                sum = sum + int(i)
            num = sum
        return num
# @lc code=end
if __name__ == "__main__":
    n = 38
    a = Solution().addDigits(n)
    print(a)