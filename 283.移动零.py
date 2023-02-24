#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while i <= n - 1:
            if nums[i] == 0:
                for j in range(i, n-1):
                    nums[j] = nums[j+1]
                nums[n-1] = 0
                n = n - 1
            else:
                i += 1


# @lc code=end
if __name__ == "__main__":
    n = [0, 1, 0, 3, 12]
    a = Solution().moveZeroes(n)
    print(a)
