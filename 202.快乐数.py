#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        index = 1
        while True:
            res = 0
            for i in range(len(n)):
                res = res + int(n[i])**2
            if res == 1:
                return True
            elif res != 1 and index < 20:
                n = str(res)
                index += 1
            else:
                return False
# @lc code=end
if __name__ == "__main__":
    n = 19
    a = Solution().isHappy(n)
    print(a)