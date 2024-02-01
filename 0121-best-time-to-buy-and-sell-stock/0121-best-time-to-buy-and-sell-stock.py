class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        l, r = 0, 1
        
        while r < len(prices):
            if prices[l]<prices[r]:
                pro = prices[r] - prices[l]
                maxPro = max(pro, maxPro)
                
            else:
                l = r
            r += 1
                
        return maxPro
                     
        