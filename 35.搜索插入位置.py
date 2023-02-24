#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        n = len(nums)
        slow = 0
        fast = n-1

        if target > nums[n-1]:
            return n
        if target < nums[0]:
            return 0

        while slow <= fast:

            index = int((slow+fast)/2)
            if target > nums[index]:
                slow = index+1
            elif target == nums[index]:
                slow = index
                fast = fast-1
            else:
                fast = index-1
        return slow


# @lc code=end
if __name__ == "__main__":
    nums1 = [1, 3, 5, 6]
    a = Solution().searchInsert(nums1, 5)
    print(a)
