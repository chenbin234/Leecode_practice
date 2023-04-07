#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1, nums2) -> List[int]:
        """_summary_

        Args:
            nums1 (_type_): _description_
            nums2 (_type_): _description_

        Returns:
            List[int]: _description_
        """
        result = []
        for i in nums1:
            if (i in nums2) and (i not in result):
                result.append(i)
        return result

# @lc code=end

