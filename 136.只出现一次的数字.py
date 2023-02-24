#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums) -> int:
        a = reduce(lambda x, y: x ^ y, nums)
        return a
        # repeat = []
        # while nums[0] in repeat or nums.count(nums[0]) != 1: 
        #     repeat.append(nums[0])
        #     nums.remove(nums[0])
        # return nums[0]

# @lc code=end
