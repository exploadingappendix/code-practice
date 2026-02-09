class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0
        r = l + 1

        while r < len(prices):
            print(r)
            gain = prices[r] - prices[l]
            if prices[r] > prices[l]:
                best = max(best,gain)
            elif prices[l] > prices[r]:
                l = r
            r += 1
        
        return best