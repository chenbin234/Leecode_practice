#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        alpha = []
        for i in range(len(pattern)):
            if pattern[i] not in alpha:
                alpha.append(pattern[i])
            else:
                

# @lc code=end
