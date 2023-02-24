#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_unique = []
        t_unique = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in s_unique and t[i] not in t_unique:
                s_unique.append(s[i])
                t_unique.append(t[i])
            elif s[i] in s_unique and t_unique[s_unique.index(s[i])] == t[i]:
                continue
            else:
                return False
        return True

# @lc code=end
if __name__ == "__main__":
    s = "badc"
    t = "baba"
    a = Solution().isIsomorphic(s,t)
    print(a)