class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        pro, maxpro = 0, 0
        
        while r < len(prices) :
            if prices[l] < prices[r]:
                pro = prices[r] - prices[l]
                maxpro = max(maxpro,pro)
            
            else:
                l = r
            r += 1
        return maxpro