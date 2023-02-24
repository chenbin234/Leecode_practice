#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = []
        for i in str(x):
            a.append(i)
        if a == a[::-1]:
            return True
        else:
            return False
# @lc code=endß

if __name__ == "__main__":
    x=13531
    print(Solution().isPalindrome(x))
