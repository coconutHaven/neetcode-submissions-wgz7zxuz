class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, buy = 0, 0
        sell = 1
        pricesLength = len(prices)
        while buy <= pricesLength - 2 and sell <= pricesLength - 1:
            if sell == buy:
                sell += 1
                continue
            profit = prices[sell] - prices[buy]

            if profit > maxProfit:
                maxProfit = profit

            ## change buy date if next day is cheaper
            if prices[buy + 1] <= prices[buy]:
                buy += 1
                continue
            
            ## check price on day after Sell
            if sell + 1 != pricesLength:
                nextSalePrice = prices[sell + 1]

                ## if price on day after sell is cheaper than current buying price
                if nextSalePrice < prices[buy]:
                    buy = sell + 1
            sell += 1

        return maxProfit



2
3
1
9
7
4

