#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return 1-nums[0]
        nums.sort()
        for i in range(n-1):
            if nums[0] != 0:
                return 0
            if nums[i+1] != nums[i]+1:
                return nums[i]+1
        return nums[-1]+1



# @lc code=end
