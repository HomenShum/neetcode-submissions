class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # given a list of int, we want to find the largest sum over all combinations of subarrays
        # how i would manually do this is literally sum up all combination keys and see how it goes 
        # borrowing the knolwedge from the two sum, we were able to get te outcome with a 
        # if comp is in the already stored seen dict, then return the current indice and the seen dict matching indice for that comp value
        # perhaps we can just iterate through all combination of loops and find the sum of each loop
        # store it as key, with the value being the subarray
        
        maxSub = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0: 
                curSum = 0 # This ensures that we get rid of the negative sums from the initial subarrays and restart from 0
            curSum += i # Continue to compute towards higher sums 
            maxSub = max(maxSub, curSum) # keep only the highest sums
        
        return maxSub # Return highest sums