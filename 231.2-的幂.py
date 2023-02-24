#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        i = 0
        while n > 2**i:
            i += 1
        if n == 2**(i):
            return True
        else:

            return False


# @lc code=end
if __name__ == "__main__":
    nums = 5
    a = Solution().isPowerOfTwo(nums)
    print(a)
