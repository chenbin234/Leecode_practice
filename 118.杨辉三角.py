#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            result = [[1],[1,1]]
            for i in range(3,numRows+1):
                row_i = [1]*i
                left = 0
                right = 1
                for k in range(1,i-1):
                    row_i[k] = result[i-2][left]+result[i-2][right]
                    row_i[i-k-1] = row_i[k]
                    left+=1
                    right+=1
                result.append(row_i)
            return result


# @lc code=end
if __name__ == "__main__":
    numRows = 5
    a = Solution().generate(numRows)
    print(a)