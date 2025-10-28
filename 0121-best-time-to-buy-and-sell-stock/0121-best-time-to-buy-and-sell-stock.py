class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy,profit = prices[0],0

        # if len(prices) == 2
        #   prices[1] > prices[0]:
        #     profit = prices[1] - prices[0]
        #     return profit
        # else:
        #     return 0
        # for i in range(len(prices)):
        #     buy = min(prices[i], buy)
        #     profit = max(profit, prices[i] - buy)
        # return profit
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

            # while prices[sell] - prices[buy] < profit and sell > buy:
            #     buy += 1 
            #     if prices[sell] - prices[buy] < profit and sell > buy:
            #         continue
            #     else:
            #          break
            # profit = prices[sell] - prices[buy]
        return profit
            