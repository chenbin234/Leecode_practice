#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums, val: int) -> int:
        self.nums = nums
        self.val = val

        n = len(nums)
        slow = 0
        fast = 0

        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


# @lc code=end
if __name__ == "__main__":
    nums1 = [3, 2, 2, 3]
    a = Solution().removeElement(nums1, 3)
    print(a)
