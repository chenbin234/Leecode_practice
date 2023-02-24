#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
# @lc code=end

if __name__ == "__main__":
    nums = [-24500,-24499,-24498,-24497,-24496,-24495,-24494,-24493,-24492,-24491,-24490,-24489,-24488,-24487,-24486,-24485,-24484,-24483,-24482,-24481,-24480,-24479,-24478,-24477,-24476,-24475,-24474,-24473,-24472,-24471,-24470,-24469,-24468,-24467]
    a = Solution().containsDuplicate(nums)
    print(a)