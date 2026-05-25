class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        res = 0 + x
        x_init = x
        
        for i in range(abs(n)-1):
            res = res * x_init
        if n < 0:
            return 1/res
        
        return res