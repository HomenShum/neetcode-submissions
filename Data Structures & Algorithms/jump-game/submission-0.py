class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel = 0
        
        for num in nums:
            # If we are out of fuel, we can't move forward
            if fuel < 0:
                return False
            
            # Take the max of our current fuel OR the new jump option
            fuel = max(fuel, num)
            
            # Burn 1 unit of fuel to move to the next position
            fuel -= 1
            
        return True