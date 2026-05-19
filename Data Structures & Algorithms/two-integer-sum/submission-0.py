class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            comp = target - n # 7-4 = 3
            if comp in seen: # {3:0} , we see comp in seen 
                return [seen[comp],i] # early return the indices [curr_i, seen_i]
            seen[n] = i # append to seen dict
