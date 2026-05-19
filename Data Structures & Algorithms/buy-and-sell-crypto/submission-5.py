class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find lowest day potential and its pos
        # then find the future highest potential after the pos
        min_p = prices[0]
        max_p = 0

        for i in prices:
            max_p = max(max_p, i - min_p) # every iteration subtract, keep max
            min_p = min(min_p, i) # make min_p lower if i smaller in newer iterations 
        return max_p