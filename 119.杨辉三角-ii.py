#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            result = [[1], [1, 1]]
            for i in range(3, rowIndex+2):
                row_i = [1]*i
                left = 0
                right = 1
                for k in range(1, i-1):
                    row_i[k] = result[i-2][left]+result[i-2][right]
                    row_i[i-k-1] = row_i[k]
                    left += 1
                    right += 1
                result.append(row_i)
            return result[-1]
# @lc code=end


if __name__ == "__main__":
    numRows = 3
    a = Solution().getRow(numRows)
    print(a)
