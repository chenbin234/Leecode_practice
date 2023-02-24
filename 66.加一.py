#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        digits = [str(i) for i in digits]
        digitstoint = int(''.join(digits))
        sum = digitstoint + 1

        result = []
        for i in str(sum):
            result.append(int(i))
        return result
            

# @lc code=end
if __name__ == "__main__":
    digits = [4,3,2,1]
    a = Solution().plusOne(digits)
    print(a)