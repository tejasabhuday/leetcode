class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        profit=0
        for i in range (1,len(prices)):
            if(prices[i]>prices[i-1]):
                profit= profit + (prices[i]-prices[i-1])
        return profit