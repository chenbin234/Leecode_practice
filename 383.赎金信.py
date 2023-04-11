#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            n = ransomNote.count(i)
            if magazine.count(i) >= n:
                continue
            else:
                return False
        return True
# @lc code=end

