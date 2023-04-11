#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for i in s:
            if i in t[index:]:
                index = index + t[index:].index(i)+1
            else:
                return False
        return True
# @lc code=end
