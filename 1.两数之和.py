#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.nums = nums
        self.target = target
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j] == target:
                    print([i,j])
                    return [i,j]
# @lc code=end

if __name__ == "__main__":
    nums1 =[1,2,3,4,5]
    target1 = 6
    Solution().twoSum(nums1, target1)