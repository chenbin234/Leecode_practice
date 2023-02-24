#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(filter(str.isalnum,s))
        new_s = new_s.lower()
        if new_s == new_s[::-1]:
            return True
        else:
            return False

# @lc code=end
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    a = Solution().isPalindrome(s)
    print(a)