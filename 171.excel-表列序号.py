#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        result = 0
        for i in range(n):
            num = ord(columnTitle[i]) - 64
            result = result + num*26**(n-i-1)
        return result
# @lc code=end
