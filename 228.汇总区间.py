#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums):
        left = 0
        right = 1
        result_list = []
        if not nums:
            return []
        res = [nums[0]]
        if len(nums) == 1:
            return ["{}".format(nums[0])]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                res.append(nums[i-1])
                res.append(nums[i])
        res.append(nums[-1])
        for j in range(0,len(res)-1,2):
            if res[j] == res[j+1]:
                result_list.append("{}".format(res[j]))
            else:
                result_list.append("{}->{}".format(res[j],res[j+1]))

        return result_list


        # i = 1
        # while nums[right] == nums[left]+i:
        #     i = i+1
        #     right = right + 1
        # res.append("{}->{}".format(nums[left], nums[right-1]))

        # left = right



# @lc code=end
if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    a = Solution().summaryRanges(nums)
    print(a)
