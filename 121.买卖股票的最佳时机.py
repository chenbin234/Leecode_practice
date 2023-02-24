#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices) -> int:

        profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            price_sell = prices[i]
            if prices[i] < min_price:
                min_price = prices[i]
            if price_sell-min_price > profit:
                profit = price_sell-min_price     
        return profit
# @lc code=end
if __name__ == "__main__":
    prices = [7,6,4,3,1]
    a = Solution().maxProfit(prices)
    print(a)