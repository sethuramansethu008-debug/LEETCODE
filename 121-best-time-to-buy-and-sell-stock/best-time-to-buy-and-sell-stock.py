class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buyprices=prices[0]
        profit=0
        for p in prices[1:]:
            if buyprices>p:
                buyprices=p
            profit=max(profit,p-buyprices)
        return profit