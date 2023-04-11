#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if t.count(i) != s.count(i):
                return i
# @lc code=end

