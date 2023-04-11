#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            n = s.count(s[i])
            if n == 1:
                return i
        return -1

# @lc code=end
