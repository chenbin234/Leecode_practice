#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split(" ")
        if len(pattern) != len(strs):
            return False

        table = {}
        for pat, st in zip(pattern, strs):
            # print(pat)
            # print(st)
            if pat not in table:
                table[pat] = st
            elif table[pat] != st:
                return False

        table = {}
        for pat, st in zip(strs, pattern):
            if pat not in table:
                table[pat] = st
            elif table[pat] != st:
                return False

        return True


# @lc code=end
