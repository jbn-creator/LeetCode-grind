class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell,profit= 0,1,0
        while sell < len(prices):

            if prices[sell] < prices[buy] and (sell - buy) == 1:
                buy += 1
                sell += 1

            elif prices[sell] < prices[buy]:
                buy += 1
                
            else:
                profit = max(profit,prices[sell] - prices[buy])
                sell += 1

        return profit
            