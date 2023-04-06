#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s) -> None:
        """This function is to reverse String

        Note:
            Do not return anything, modify s in-place instead.

        Args:
            s (List[str]): the string
        """

        n = len(s)
        if n % 2 == 0:
            n_length = n//2
        else:
            n_length = (n-1)//2

        for i in range(n_length):
            temp = s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = temp

# @lc code=end
