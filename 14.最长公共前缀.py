#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start

from genericpath import exists


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        else:   
            commonprefix = []
            n = 1
            for i in range(len(strs[0])):
                for j in range(1,len(strs)):
                    if len(strs[j]) > i and strs[0][i] == strs[j][i]: 
                        n += 1
                    else:
                        return ''.join(commonprefix)
                if n == len(strs):
                    commonprefix.append(strs[0][i])   
                n = 1
            return (''.join(commonprefix))
# @lc code=end

if __name__ == "__main__":
    strs = ['abc','abd','abcd']
    Solution().longestCommonPrefix(strs)

