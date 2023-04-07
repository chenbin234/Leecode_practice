#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """_summary_

        Args:
            nums1 (List[int]): _description_
            nums2 (List[int]): _description_

        Returns:
            List[int]: _description_
        """
        result = []
        for i in nums1:
            if (i in nums2) and (nums2.count(i) > result.count(i)):
                result.append(i)
        return result
# @lc code=end

