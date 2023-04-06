#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums):
        self.nums = nums


    def sumRange(self, left: int, right: int) -> int:
        result = 0
        for i in range(left,right+1):
            result = result + self.nums[i]
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

