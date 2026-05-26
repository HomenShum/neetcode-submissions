class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # keep track of x and y 
        # return top sorted y and their location x
        # find max combinations of multiplications 
        # however, if the two y is not equal, then use min y
        
        l = 0
        res = 0

        r = len(heights)-1

        while r > l:
            res = max(res, min(heights[l],heights[r]) * (r-l))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        # for l in range(len(heights)):
        #     for r in range(len(heights)):
        #         res = max(res, min(heights[l],heights[r]) * (r-l))
        
        return res