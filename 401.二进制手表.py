#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int):
        result = []
        hours = [1, 2, 4, 8]
        minutes = [1,2,4,8,16,32]
        if turnedOn > 8:
            return result
        if turnedOn == 0:
            return ["0:00"]
        for i in turnedOn+1:
            hour_led = i
            min_led = turnedOn-1
            


# @lc code=end
