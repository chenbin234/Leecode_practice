#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack
# @lc code=end
if __name__ == "__main__":

    s1 = '({}()()[])'
    Solution().isValid(s1)