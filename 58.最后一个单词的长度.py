#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        s = s.split()[-1]
        return len(s)


# @lc code=end
if __name__ == "__main__":
    s = "luffy is still joyboy"
    a = Solution().lengthOfLastWord(s)
    print(a)
