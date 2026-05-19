class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        if len(set(nums)) == len(nums):
            for i in nums:
                prod = 1
                for j in nums:
                    if j != i:
                        prod *= j
                res.append(prod)
                # but the problem is with duplicates
                # alternatively we can track all pos instead
        else:
            # track pos if duplicates show up
            for i, iv in enumerate(nums):
                tracker_list = []
                for j, jv in enumerate(nums):
                    if i != j:
                        tracker_list.append(jv)
                import math
                res.append(math.prod(tracker_list))
        
        return res
