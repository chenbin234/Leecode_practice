#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """_summary_

        Args:
            num (int): _description_

        Returns:
            bool: _description_
        """
        i = 1
        while i*i <= num:
            if i*i == num:
                return True
            i += 1
        return False
# @lc code=end

