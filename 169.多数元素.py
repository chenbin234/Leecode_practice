#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums) -> int:
        n = len(nums)
        blacket = []
        
        for i in nums:
            if i in blacket:
                pass
            elif nums.count(i) > n/2:
                return i
            elif nums.count(i) <= n/2 and i not in blacket:
                blacket.append(i)

# @lc code=end

