#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n) -> int:
        return int("0b"+("0"*32+bin(n)[2:])[-32:][::-1], base=2)


        # n = str(n)
        # list = [int(x) for x in n]
        # print(list)
        # list = list[::-1]
        # result = ''
        # for i in list:
        #     result = result + str(i)
        # return str(int(str(result),2)) + ' ' + ("({})").format(result)
# @lc code=end
if __name__ == "__main__":
    n = '00000010100101000001111010011100'
    a = Solution().reverseBits(n)
    print(a)
