class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy, sell = 0, 1
        pricesLength = len(prices)
        while sell < pricesLength:
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(profit, maxProfit)
            else: 
                buy = sell
            sell += 1

        return maxProfit



2
3
1
9
7
4

