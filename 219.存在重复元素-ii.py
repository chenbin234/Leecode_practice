#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums, k: int):
        # n = len(nums)
        # left = 0
        # right = min(n,k+1)
        # while right <= n:
        #     check_list = nums[left:right]
        #     check_list.sort()
        #     m = len(check_list)
        #     for j in range(m-1):
        #         if check_list[j] == check_list[j+1]:
        #             return True
        #     left += 1
        #     right += 1
        # return False
        s = set()
        for i, num in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)
        return False


# @lc code=end


if __name__ == "__main__":
    nums = [99,99]
    k = 3
    a = Solution().containsNearbyDuplicate(nums, k)
    print(a)
