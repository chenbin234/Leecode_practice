#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """This is a function to check whether a number is power of 4 or not

        Args:
            n (int): input number

        Returns:
            bool: the result
        """   
        if n <=0:
            return False
        if n == 1:
            return True
             
        while n >= 2:
            if n % 4 != 0:
                return False
            else:
                n = n/4
        return True



# @lc code=end
