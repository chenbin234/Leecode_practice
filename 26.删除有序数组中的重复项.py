#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        self.nums = nums
        x = 1
        for i in range(len(nums)-1):
            if(nums[i] != nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        return len(nums[0:x])
# @lc code=end


if __name__ == "__main__":
    nums1 = [1,1]
    a = Solution().removeDuplicates(nums1)
    print(a)
